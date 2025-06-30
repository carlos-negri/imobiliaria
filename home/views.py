from django.views.generic import TemplateView

from imoveis.models import Imovel


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ultimos_imoveis'] = Imovel.objects.all().order_by('-id')[:4]
        return context
