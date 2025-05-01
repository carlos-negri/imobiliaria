from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import VisitaModelForm
from .models import Visita
from django.core.paginator import Paginator
from django.contrib import messages

class VisitaView(ListView):
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


class VisitaAddView(SuccessMessageMixin,CreateView):
    model = Visita
    form_class = VisitaModelForm
    template_name = 'visitas_form.html'
    success_url = reverse_lazy('visitas')
    success_message = 'Visita agendada com sucesso'

class VisitaUpdateView(SuccessMessageMixin,UpdateView):
    model = Visita
    form_class = VisitaModelForm
    template_name = 'visitas_form.html'
    success_url = reverse_lazy('visitas')
    success_message = 'Visita atualizada com sucesso'

class VisitaDeleteView(SuccessMessageMixin, DeleteView):
    model = Visita
    template_name = 'visita_apagar.html'
    success_url = reverse_lazy('visitas')
    success_message = 'Visita cancelada com sucesso'