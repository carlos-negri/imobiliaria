from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateResponseMixin, View
from .forms import ProprietarioModelForm, ImoveisProprietarioInLine
from .models import Proprietario, ImoveisProprietario
from django.core.paginator import Paginator
from django.contrib import messages

class ProprietarioView(PermissionRequiredMixin,ListView):
    permission_required = 'proprietarios.view_proprietario'
    permission_denied_message = 'Visualizar proprietário'
    model = Proprietario
    template_name = 'proprietarios.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(ProprietarioView, self).get_queryset()
        if buscar:
            qs = qs.filter(nome__icontains=buscar)

        for proprietario in qs:
            imovel = ImoveisProprietario.objects.filter(proprietario=proprietario)
            imovel.proprietario = imovel

        if qs.count()>0:
            paginator = Paginator(qs, 10)
            listagem =paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, 'Não existem proprietários cadastrados!')


class ProprietarioAddView(PermissionRequiredMixin,SuccessMessageMixin,CreateView):
    permission_required = 'proprietarios.add_proprietario'
    permission_denied_message = 'Cadastrar proprietário'
    model = Proprietario
    form_class = ProprietarioModelForm
    template_name = 'proprietario_form.html'
    success_url = reverse_lazy('proprietarios')
    success_message = 'Proprietário cadastrado com sucesso'

class ProprietarioUpdateView(PermissionRequiredMixin,SuccessMessageMixin, UpdateView):
    permission_required = 'proprietarios.update_proprietario'
    permission_denied_message = 'Editar proprietário'
    model = Proprietario
    form_class = ProprietarioModelForm
    template_name = 'proprietario_form.html'
    success_url = reverse_lazy('proprietarios')
    success_message = 'Proprietário atualizado com sucesso'

class ProprietarioDeleteView(PermissionRequiredMixin,SuccessMessageMixin, DeleteView):
    permission_required = 'proprietarios.delete_proprietario'
    permission_denied_message = 'Excluir proprietário'
    model = Proprietario
    template_name = 'proprietario_apagar.html'
    success_url = reverse_lazy('proprietarios')
    success_message = 'Proprietário apagado com sucesso'

class ProprietarioInLineEditView(PermissionRequiredMixin,TemplateResponseMixin, View):
    permission_required = 'proprietarios.inline_proprietario'
    permission_denied_message = 'Você não tem permissão para acessar este módulo'
    template_name = 'proprietario_inline.html'

    def get_formset(self, data=None):
        return ImoveisProprietarioInLine(instance=self.proprietario, data=data)


    def dispatch (self, request, pk):
        self.proprietario = get_object_or_404(Proprietario, id=pk)
        return super().dispatch(request, pk)


    def get(self, request, *args, **kwargs):
        formset = self.get_formset()
        return self.render_to_response({'proprietario': self.proprietario, 'formset': formset})

    def post(self, request, *args, **kwargs):
        formset = self.get_formset(data=request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('proprietarios')
        return self.render_to_response({'proprietario': self.proprietario, 'formset': formset})