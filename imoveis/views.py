from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, render
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import ImovelModelForm
from .models import Imovel
from django.core.paginator import Paginator
from django.contrib import messages

class ImovelView(ListView):
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


class ImovelAddView(SuccessMessageMixin,CreateView):
    model = Imovel
    form_class = ImovelModelForm
    template_name = 'imovel_form.html'
    success_url = reverse_lazy('imoveis')
    success_message = 'Imóvel cadastrado com sucesso'

class ImovelUpdateView(SuccessMessageMixin, UpdateView):
    model = Imovel
    form_class = ImovelModelForm
    template_name = 'imovel_form.html'
    success_url = reverse_lazy('imoveis')
    success_message = 'Imóvel atualizado com sucesso'

class ImovelDeleteView(SuccessMessageMixin, DeleteView):
    model = Imovel
    template_name = 'imovel_apagar.html'
    success_url = reverse_lazy('imoveis')
    success_message = 'Imóvel apagado com sucesso'

def exibir_imovel(request, pk):
    imovel = get_object_or_404(Imovel, pk=pk)
    return render(request, 'imovel_exibir.html', {'imovel': imovel})