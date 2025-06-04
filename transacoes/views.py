from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.template.loader import render_to_string
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

    def post (self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            transacao = form.save(commit=True)
            if transacao:
                self.enviar_email(transacao)
        return redirect('transacoes')

    def enviar_email(self, transacao):
        email = []
        email.append(transacao.cliente.email)

        dados = {'cliente': transacao.cliente.nome,
                 'proprietario': transacao.proprietario.nome,
                 'imovel':transacao.imovel,
                 'endereco': transacao.imovel.endereco,
                 'corretor': transacao.corretor.nome,
                 'tipo': transacao.get_tipo_display,
                 'valor': transacao.valor,
                 }

        texto_email = render_to_string('emails/texto.txt', dados)
        html_email = render_to_string('emails/texto.html', dados)
        send_mail(subject='JATIMOV - Parabéns!',
                  message = texto_email,
                  from_email = 'chnnegri@gmail.com',
                  recipient_list = email,
                  html_message = html_email,
                  fail_silently = False,
        )
        return redirect('transacoes')


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

