from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Subquery, Q
from django.shortcuts import get_object_or_404, render, redirect
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.views.generic.base import TemplateResponseMixin, View, TemplateView

from transacoes.models import Transacao
from .forms import ImovelEtapa2Form, ImovelEtapa1Form, ImovelModelForm
from .models import Imovel
from django.core.paginator import Paginator
from django.contrib import messages

class ImovelView(PermissionRequiredMixin, ListView):
    permission_required = 'imoveis.view_imovel'
    permission_denied_message = 'Visualizar imóvel'
    model = Imovel
    template_name = 'imoveis.html'



class ImovelAddEtapa1View(PermissionRequiredMixin, FormView):
    permission_required = 'imoveis.add_imovel'
    template_name = 'imovel_form_1.html'
    form_class = ImovelEtapa1Form

    def form_valid(self, form):
        self.request.session['dados_etapa1'] = form.cleaned_data
        return redirect('imovel_add_etapa2')

class ImovelAddEtapa2View(PermissionRequiredMixin, FormView):
    permission_required = 'imoveis.add_imovel'
    template_name = 'imovel_form_2.html'
    form_class = ImovelEtapa2Form

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['dados_etapa1'] = self.request.session.get('dados_etapa1', {})
        return kwargs

    def form_valid(self, form):
        dados_etapa1 = self.request.session.get('dados_etapa1')

        if not dados_etapa1:
            messages.error(self.request, 'Erro: dados da primeira etapa não encontrados.')
            return redirect('imovel_add_etapa1')

        tipo_aluguel = dados_etapa1.get('tipo_aluguel')
        status_imovel = form.cleaned_data.get('status_imovel')

        if tipo_aluguel and status_imovel in ['PLANTA', 'CONSTR']:
            form.add_error('status_imovel',
                           'Imóveis na planta ou em construção não podem ser cadastrados para aluguel.')
            return self.form_invalid(form)


        proprietarios = form.cleaned_data.pop('proprietarios')


        imovel = Imovel(**dados_etapa1, **form.cleaned_data)
        imovel.save()


        imovel.proprietarios.set(proprietarios)
        return redirect('imoveis')

class ImovelUpdateView(PermissionRequiredMixin,SuccessMessageMixin, UpdateView):
    permission_required = 'imoveis.update_imovel'
    permission_denied_message = 'Editar imóvel'
    model = Imovel
    form_class = ImovelModelForm
    template_name = 'imovel_form_edit.html'
    success_url = reverse_lazy('imoveis')
    success_message = 'Imóvel atualizado com sucesso'

class ImovelDeleteView(PermissionRequiredMixin,SuccessMessageMixin, DeleteView):
    permission_required = 'imoveis.delete_imovel'
    permission_denied_message = 'Excluir imóvel'
    model = Imovel
    template_name = 'imovel_apagar.html'
    success_url = reverse_lazy('imoveis')
    success_message = 'Imóvel apagado com sucesso'

def exibir_imovel(request, pk):
    imovel = get_object_or_404(Imovel, pk=pk)
    return render(request, 'imovel_exibir.html', {'imovel': imovel})


class ImovelDisponivelView(ListView):
    model = Imovel
    template_name = 'imoveis.html'
    context_object_name = 'object_list'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar', '')
        tipo = self.request.GET.get('tipo', '')  # Captura o tipo do filtro (aluguel ou venda)

        imoveis_com_transacao = Transacao.objects.values('imovel_id')
        qs = Imovel.objects.exclude(id__in=Subquery(imoveis_com_transacao))

        # Filtro por tipo (aluguel ou venda)
        if tipo == 'aluguel':
            qs = qs.filter(tipo_aluguel=True)
        elif tipo == 'venda':
            qs = qs.filter(tipo_venda=True)

        # Filtro por busca (endereço)
        if buscar:
            qs = qs.filter(
                Q(imovel__endereco__icontains=buscar),
                Q(imovel__endereco__icontains=buscar)
            )

        return qs