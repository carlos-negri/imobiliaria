from collections import namedtuple

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.db.models import Q
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import VisitaModelForm, VisitaUpdateModelForm
from .models import Visita
from django.core.paginator import Paginator
from django.contrib import messages
import calendar

class VisitaView(PermissionRequiredMixin, ListView):
    permission_required = 'visita.view_visita'
    permission_denied_message = 'Visualizar visita'
    model = Visita
    template_name = 'visitas.html'

    def get_queryset(self):
        qs = super().get_queryset()

        buscar = self.request.GET.get('buscar', '').strip()
        filtro_mes = self.request.GET.get('mes', '').strip().lower()
        filtro_dia_semana = self.request.GET.get('dia_semana', '').strip().lower()
        filtro_situacao = self.request.GET.get('situacao', '').strip().upper()

        if buscar:
            qs = qs.filter(
                Q(cliente__nome__icontains=buscar) |
                Q(imovel__codigo_unico__icontains=buscar) |
                Q(corretor__nome__icontains=buscar)
            )

        if filtro_mes:
            meses_pt = {
                'janeiro': 1, 'fevereiro': 2, 'março': 3, 'abril': 4,
                'maio': 5, 'junho': 6, 'julho': 7, 'agosto': 8,
                'setembro': 9, 'outubro': 10, 'novembro': 11, 'dezembro': 12,
            }
            num_mes = meses_pt.get(filtro_mes)
            if num_mes:
                qs = qs.filter(datahora__month=num_mes)

        if filtro_dia_semana:
            dias_semana = {
                'domingo': 1,
                'segunda-feira': 2, 'segunda': 2,
                'terça-feira': 3, 'terça': 3,
                'quarta-feira': 4, 'quarta': 4,
                'quinta-feira': 5, 'quinta': 5,
                'sexta-feira': 6, 'sexta': 6,
                'sábado': 7, 'sabado': 7,
            }
            num_dia = dias_semana.get(filtro_dia_semana)
            if num_dia:
                qs = qs.filter(datahora__week_day=num_dia)

        if filtro_situacao:
            qs = qs.filter(situacao=filtro_situacao)

        if qs.exists():
            paginator = Paginator(qs, 10)
            return paginator.get_page(self.request.GET.get('page'))
        else:
            messages.info(self.request, 'Não existem visitas agendadas!')
            return qs.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        meses_pt = [
            (1, 'Janeiro'),
            (2, 'Fevereiro'),
            (3, 'Março'),
            (4, 'Abril'),
            (5, 'Maio'),
            (6, 'Junho'),
            (7, 'Julho'),
            (8, 'Agosto'),
            (9, 'Setembro'),
            (10, 'Outubro'),
            (11, 'Novembro'),
            (12, 'Dezembro'),
        ]
        context['meses'] = meses_pt

        Dia = namedtuple('Dia', ['value', 'display'])
        context['dias_semana'] = [
            Dia('domingo', 'Domingo'),
            Dia('segunda-feira', 'Segunda-feira'),
            Dia('terça-feira', 'Terça-feira'),
            Dia('quarta-feira', 'Quarta-feira'),
            Dia('quinta-feira', 'Quinta-feira'),
            Dia('sexta-feira', 'Sexta-feira'),
            Dia('sábado', 'Sábado'),
        ]

        context['situacoes'] = Visita.SITUACAO_CHOICES

        return context

class VisitaAddView(PermissionRequiredMixin,SuccessMessageMixin,CreateView):
    permission_required = 'visita.add_visita'
    permission_denied_message = 'Cadastrar visita'
    model = Visita
    form_class = VisitaModelForm
    template_name = 'visitas_form.html'
    success_url = reverse_lazy('visitas')
    success_message = 'Visita agendada com sucesso'


    def post (self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            visita = form.save(commit=True)

            if visita.situacao == 'A':
                self.enviar_email(visita)
            return redirect('visitas')


    def enviar_email(self, visita):
        email = []
        email.append(visita.cliente.email)

        dados = {'cliente': visita.cliente.nome,
                 'imovel':visita.imovel,
                 'datahora': visita.datahora,
                 'corretor': visita.corretor.nome,
                 }

        texto_email = render_to_string('emails/email_confirma.txt', dados)
        html_email = render_to_string('emails/email_confirma.html', dados)
        send_mail(subject='JATIMOV - Visita Agendada',
                  message = texto_email,
                  from_email = 'chnnegri@gmail.com',
                  recipient_list = email,
                  html_message = html_email,
                  fail_silently = False,
        )
        return redirect('visitas')

class VisitaUpdateView(PermissionRequiredMixin,SuccessMessageMixin,UpdateView):
    permission_required = 'visita.update_visita'
    permission_denied_message = 'Editar visita'
    model = Visita
    form_class = VisitaUpdateModelForm
    template_name = 'visitas_form.html'
    success_url = reverse_lazy('visitas')
    success_message = 'Visita atualizada com sucesso'

class VisitaDeleteView(PermissionRequiredMixin,SuccessMessageMixin, DeleteView):
    permission_required = 'visita.delete_visita'
    permission_denied_message = 'Excluir visita'
    model = Visita
    template_name = 'visita_apagar.html'
    success_url = reverse_lazy('visitas')
    success_message = 'Visita cancelada com sucesso'

class VisitaExibir(DetailView):
    model = Visita
    template_name = 'visita_exibir.html'

    def get_object(self, queryset=None):
        visita = Visita.objects.get(pk=self.kwargs.get('pk'))
        visita.situacao = 'CO'
        visita.save()
        self.enviar_email(visita)
        return visita

    def enviar_email(self, visita):
        email = []
        email.append(visita.cliente.email)

        dados = {'cliente': visita.cliente.nome,
                 'imovel':visita.imovel,
                 'datahora': visita.datahora,
                 'corretor': visita.corretor.nome,
                 }

        texto_email = render_to_string('emails/texto_email.txt', dados)
        html_email = render_to_string('emails/texto_email.html', dados)
        send_mail(subject='JATIMOV - Visita Concluída',
                  message = texto_email,
                  from_email = 'chnnegri@gmail.com',
                  recipient_list = email,
                  html_message = html_email,
                  fail_silently = False,
        )
        return redirect('visitas')