from django.shortcuts import render, get_object_or_404
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import TransacaoModelForm
from .models import Transacao

class TransacaoView(ListView):
    model = Transacao
    template_name = 'transacoes.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(TransacaoView, self).get_queryset()
        if buscar:
            qs = qs.filter(codigo_unico__icontains=buscar)
        if qs.count()>0:
            paginator = Paginator(qs, 10)
            listagem =paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, 'Não existem transações cadastradas!')

class TransacaoAddView(SuccessMessageMixin,CreateView):
    model = Transacao
    form_class = TransacaoModelForm
    template_name = 'transacao_form.html'
    success_url = reverse_lazy('transacoes')


class AluguelAddView(SuccessMessageMixin,CreateView):
    model = Transacao
    form_class = TransacaoModelForm
    template_name = 'transacao_aluguel.html'
    success_url = reverse_lazy('transacoes')
    success_message = 'Aluguel cadastrado com sucesso'

class VendaAddView(SuccessMessageMixin,CreateView):
    model = Transacao
    form_class = TransacaoModelForm
    template_name = 'transacao_venda.html'
    success_url = reverse_lazy('transacoes')
    success_message = 'Venda cadastrada com sucesso'

class TransacaoUpdateView(SuccessMessageMixin,UpdateView):
    model = Transacao
    form_class = TransacaoModelForm
    template_name = 'transacao_form.html'
    success_url = reverse_lazy('transacoes')
    success_message = 'Transacão atualizada com sucesso'

class TransacaoDeleteView(SuccessMessageMixin, DeleteView):
    model = Transacao
    template_name = 'transacao_apagar.html'
    success_url = reverse_lazy('transacoes')
    success_message = 'Transação anulada com sucesso'

def exibir_transacao(request, pk):
    transacao = get_object_or_404(Transacao, pk=pk)
    return render(request, 'transacao_exibir.html', {'transacao': transacao})

class SelecionarTipoView(ListView):
    model = Transacao
    template_name = 'transacao_form.html'