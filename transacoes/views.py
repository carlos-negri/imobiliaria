from django.contrib.auth.mixins import PermissionRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.messages.views import SuccessMessageMixin
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, FormView
from django.core.paginator import Paginator
from django.contrib import messages
from .forms import TransacaoModelForm, TransacaoEtapa1Form, TransacaoEtapa2Form
from .models import Transacao
from django.db.models import Q

class TransacaoView(PermissionRequiredMixin,ListView):
    permission_required = 'transacoes.view_transacao'
    permission_denied_message = 'Visualizar transação'
    model = Transacao
    template_name = 'transacoes.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(TransacaoView, self).get_queryset()
        if buscar:
            qs = qs.filter(
                Q(proprietario__nome__icontains=buscar) |
                Q(cliente__nome__icontains=buscar) |
                Q(corretor__nome__icontains=buscar)
            )
        if qs.count()>0:
            paginator = Paginator(qs, 10)
            listagem =paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, 'Não existem transações cadastradas!')

class TransacaoAddEtapa1View(PermissionRequiredMixin, FormView):
    permission_required = 'transacoes.add_transacao'
    template_name = 'transacao_form_1.html'
    form_class = TransacaoEtapa1Form

    def form_valid(self, form):
        self.request.session['dados_etapa1'] = form.cleaned_data
        return redirect('transacao_add_etapa2')

class TransacaoAddEtapa2View(PermissionRequiredMixin, FormView):
    permission_required = 'transacoes.add_transacao'
    template_name = 'transacao_form_2.html'
    form_class = TransacaoEtapa2Form

    def form_valid(self, form):
        dados_etapa1 = self.request.session.get('dados_etapa1')

        if not dados_etapa1:
            messages.error(self.request, 'Erro: dados da primeira etapa não encontrados.')
            return redirect('transacao_add_etapa1')

        transacao = Transacao(**dados_etapa1, **form.cleaned_data)
        transacao.save()
        messages.success(self.request, 'Transação cadastrada com sucesso.')
        return redirect('transacoes')

class TransacaoAddView(PermissionRequiredMixin,SuccessMessageMixin,CreateView):
    permission_required = 'transacoes.add_transacao'
    permission_denied_message = 'Cadastrar transação'
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


class TransacaoUpdateView(PermissionRequiredMixin,SuccessMessageMixin,UpdateView):
    permission_required = 'transacoes.update_transacao'
    permission_denied_message = 'Editar transação'
    model = Transacao
    form_class = TransacaoModelForm
    template_name = 'transacao_form.html'
    success_url = reverse_lazy('transacoes')
    success_message = 'Transacão atualizada com sucesso'

class TransacaoDeleteView(PermissionRequiredMixin,SuccessMessageMixin, DeleteView):
    permission_required = 'transacoes.delete_transacao'
    permission_denied_message = 'Excluir transação'
    model = Transacao
    template_name = 'transacao_apagar.html'
    success_url = reverse_lazy('transacoes')
    success_message = 'Transação anulada com sucesso'

def exibir_transacao(request, pk):
    transacao = get_object_or_404(Transacao, pk=pk)
    return render(request, 'transacao_exibir.html', {'transacao': transacao})

