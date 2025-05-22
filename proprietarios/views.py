from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateResponseMixin, View
from .forms import ProprietarioModelForm, ImoveisProprietarioInLine
from .models import Proprietario
from django.core.paginator import Paginator
from django.contrib import messages

class ProprietarioView(ListView):
    model = Proprietario
    template_name = 'proprietarios.html'

    def get_queryset(self):
        buscar = self.request.GET.get('buscar')
        qs = super(ProprietarioView, self).get_queryset()
        if buscar:
            qs = qs.filter(nome__icontains=buscar)
        if qs.count()>0:
            paginator = Paginator(qs, 10)
            listagem =paginator.get_page(self.request.GET.get('page'))
            return listagem
        else:
            return messages.info(self.request, 'Não existem proprietários cadastrados!')


class ProprietarioAddView(SuccessMessageMixin,CreateView):
    model = Proprietario
    form_class = ProprietarioModelForm
    template_name = 'proprietario_form.html'
    success_url = reverse_lazy('proprietarios')
    success_message = 'Proprietário cadastrado com sucesso'

class ProprietarioUpdateView(SuccessMessageMixin, UpdateView):
    model = Proprietario
    form_class = ProprietarioModelForm
    template_name = 'proprietario_form.html'
    success_url = reverse_lazy('proprietarios')
    success_message = 'Proprietário atualizado com sucesso'

class ProprietarioDeleteView(SuccessMessageMixin, DeleteView):
    model = Proprietario
    template_name = 'proprietario_apagar.html'
    success_url = reverse_lazy('proprietarios')
    success_message = 'Proprietário apagado com sucesso'

class ProprietarioInLineEditView(TemplateResponseMixin, View):
    template_name = 'proprietario_inline.html'

    def get_formset(self, data=None):
        return ImoveisProprietarioInLine(instance=self.proprietario, data=data)


    def dispatch (self, request, pk):
        self.proprietario = get_object_or_404(Proprietario, id=pk)
        return super().dispatch(request, pk)


    def get(self, request, *args, **kwargs):
        formset = self.get_formset()
        return self.render_to_response({'proprietario': self.proprietario, 'formset': formset})

    def post(self, request, *args, **kwargs):
        formset = self.get_formset(data=request.POST)
        if formset.is_valid():
            formset.save()
            return redirect('proprietarios')
        return self.render_to_response({'proprietario': self.proprietario, 'formset': formset})