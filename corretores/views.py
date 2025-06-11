from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import CorretorModelForm
from .models import Corretor
from django.core.paginator import Paginator
from django.contrib import messages

class CorretorView(PermissionRequiredMixin,ListView):
    permission_required = 'corretores.view_corretor'
    permission_denied_message = 'Visualizar corretor'
    model = Corretor
    template_name = "corretores.html"

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(CorretorView, self).get_queryset()
        if buscar:
            qs = qs.filter(nome__icontains=buscar)
        if qs.count() > 0:
            paginator = Paginator(qs, 10)
            listagem = paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, 'Não existem corretores cadastrados!')


class CorretorAddView(PermissionRequiredMixin,SuccessMessageMixin, CreateView):
    permission_required = 'corretores.add_corretor'
    permission_denied_message = 'Adicionar corretor'
    model = Corretor
    form_class = CorretorModelForm
    template_name = 'corretor_form.html'
    success_url = reverse_lazy('corretores')
    success_message = 'Corretor cadastrado com sucesso'


class CorretorUpdateView(PermissionRequiredMixin,SuccessMessageMixin, UpdateView):
    permission_required = 'corretores.update_corretor'
    permission_denied_message = 'Editar corretor'
    model = Corretor
    form_class = CorretorModelForm
    template_name = 'corretor_form.html'
    success_url = reverse_lazy('corretores')
    success_message = 'Corretor atualizado com sucesso'


class CorretorDeleteView(PermissionRequiredMixin,SuccessMessageMixin, DeleteView):
    permission_required = 'corretores.delete_corretor'
    permission_denied_message = 'Excluir corretor'
    model = Corretor
    template_name = 'corretor_apagar.html'
    success_url = reverse_lazy('corretores')
    success_message = 'Corretor apagado com sucesso'