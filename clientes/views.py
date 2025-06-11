from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import ClienteModelForm
from .models import Cliente
from django.core.paginator import Paginator
from django.contrib import messages

class ClienteView(ListView):
    permission_required = 'clientes.view_cliente'
    permission_denied_message = 'Visualizar cliente'
    model = Cliente
    template_name = 'clientes.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(ClienteView, self).get_queryset()
        if buscar:
            qs = qs.filter(nome__icontains=buscar)
        if qs.count()>0:
            paginator = Paginator(qs, 10)
            listagem =paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, 'Não existem clientes cadastrados!')


class ClienteAddView(SuccessMessageMixin,CreateView):
    permission_required = 'clientes.add_cliente'
    permission_denied_message = 'Cadastrar cliente'
    model = Cliente
    form_class = ClienteModelForm
    template_name = 'cliente_form.html'
    success_url = reverse_lazy('clientes')
    success_message = 'Cliente cadastrado com sucesso'

class ClienteUpdateView(SuccessMessageMixin,UpdateView):
    permission_required = 'clientes.update_cliente'
    permission_denied_message = 'Editar cliente'
    model = Cliente
    form_class = ClienteModelForm
    template_name = 'cliente_form.html'
    success_url = reverse_lazy('clientes')
    success_message = 'Cliente atualizado com sucesso'

class ClienteDeleteView(SuccessMessageMixin, DeleteView):
    permission_required = 'clientes.delete_cliente'
    permission_denied_message = 'Excluir cliente'
    model = Cliente
    template_name = 'cliente_apagar.html'
    success_url = reverse_lazy('clientes')
    success_message = 'Cliente apagado com sucesso'