from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, render, redirect
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateResponseMixin, View, TemplateView

from .forms import ImovelModelForm
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


class ImovelAddView(PermissionRequiredMixin,SuccessMessageMixin,CreateView):
    permission_required = 'imoveis.add_imovel'
    permission_denied_message = 'Cadastrar imóvel'
    model = Imovel
    form_class = ImovelModelForm
    template_name = 'imovel_form.html'
    success_url = reverse_lazy('imoveis')
    success_message = 'Imóvel cadastrado com sucesso'

class ImovelUpdateView(PermissionRequiredMixin,SuccessMessageMixin, UpdateView):
    permission_required = 'imoveis.update_imovel'
    permission_denied_message = 'Editar imóvel'
    model = Imovel
    form_class = ImovelModelForm
    template_name = 'imovel_form.html'
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


