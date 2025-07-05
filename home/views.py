from django.db.models import Subquery
from django.views.generic import TemplateView

from imoveis.models import Imovel
from transacoes.models import Transacao


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        imoveis_com_transacao = Transacao.objects.values('imovel_id')
        context['ultimos_imoveis'] = Imovel.objects.exclude(id__in=Subquery(imoveis_com_transacao))
        return context
