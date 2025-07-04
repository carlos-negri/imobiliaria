from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, render, redirect
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.views.generic.base import TemplateResponseMixin, View, TemplateView

from .forms import ImovelEtapa2Form, ImovelEtapa1Form, ImovelModelForm
from .models import Imovel
from django.core.paginator import Paginator
from django.contrib import messages

class ImovelView(PermissionRequiredMixin, ListView):
    permission_required = 'imoveis.view_imovel'
    permission_denied_message = 'Visualizar imóvel'
    model = Imovel
    template_name = 'imoveis.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(ImovelView, self).get_queryset()
        if buscar:
            qs = qs.filter(codigo_unico__icontains=buscar)
        if qs.count()>0:
            paginator = Paginator(qs, 10)
            listagem =paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, 'Não existem imóveis cadastrados!')


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

    def form_valid(self, form):
        dados_etapa1 = self.request.session.get('dados_etapa1')

        if not dados_etapa1:
            messages.error(self.request, 'Erro: dados da primeira etapa não encontrados.')
            return redirect('imovel_add_etapa1')

        imovel = Imovel(**dados_etapa1, **form.cleaned_data)
        imovel.save()
        messages.success(self.request, 'Imóvel cadastrado com sucesso.')
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


