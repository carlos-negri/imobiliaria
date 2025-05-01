from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import CorretorModelForm
from .models import Corretor
from django.core.paginator import Paginator
from django.contrib import messages

class CorretorView(ListView):
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


class CorretorAddView(SuccessMessageMixin, CreateView):
    model = Corretor
    form_class = CorretorModelForm
    template_name = 'corretor_form.html'
    success_url = reverse_lazy('corretores')
    success_message = 'Corretor cadastrado com sucesso'


class CorretorUpdateView(SuccessMessageMixin, UpdateView):
    model = Corretor
    form_class = CorretorModelForm
    template_name = 'corretor_form.html'
    success_url = reverse_lazy('corretores')
    success_message = 'Corretor atualizado com sucesso'


class CorretorDeleteView(SuccessMessageMixin, DeleteView):
    model = Corretor
    template_name = 'corretor_apagar.html'
    success_url = reverse_lazy('corretores')
    success_message = 'Corretor apagado com sucesso'