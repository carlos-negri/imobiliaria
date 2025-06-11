from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .forms import VisitaModelForm
from .models import Visita
from django.core.paginator import Paginator
from django.contrib import messages

class VisitaView(PermissionRequiredMixin,ListView):
    permission_required = 'visitas.view_visita'
    permission_denied_message = 'Visualizar visita'
    model = Visita
    template_name = 'visitas.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(VisitaView, self).get_queryset()
        if buscar:
            qs = qs.filter(nome__icontains=buscar)
        if qs.count()>0:
            paginator = Paginator(qs, 10)
            listagem =paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, 'Não existem visitas agendadas!')


class VisitaAddView(PermissionRequiredMixin,SuccessMessageMixin,CreateView):
    permission_required = 'visitas.add_visita'
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
    permission_required = 'visitas.update_visita'
    permission_denied_message = 'Editar visita'
    model = Visita
    form_class = VisitaModelForm
    template_name = 'visitas_form.html'
    success_url = reverse_lazy('visitas')
    success_message = 'Visita atualizada com sucesso'

class VisitaDeleteView(PermissionRequiredMixin,SuccessMessageMixin, DeleteView):
    permission_required = 'visitas.delete_visita'
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
        if visita.situacao!='CO':
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