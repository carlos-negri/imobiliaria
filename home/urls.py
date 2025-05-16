from django.urls import path

from imoveis.views import ImovelView
from transacoes.views import TransacaoView
from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('imoveis', ImovelView.as_view(), name='imoveis'),
    path('imoveis', TransacaoView.as_view(), name='transacoes'),

]