from django.urls import path
from .views import TransacaoView, TransacaoUpdateView, TransacaoDeleteView, exibir_transacao, TransacaoAddEtapa1View, TransacaoAddEtapa2View

urlpatterns = [
    path('transacoes', TransacaoView.as_view(), name='transacoes'),
    path('transacao/adicionar/', TransacaoAddEtapa1View.as_view(), name='transacao_add_etapa1'),
    path('transacao/adicionar/dados/', TransacaoAddEtapa2View.as_view(), name='transacao_add_etapa2'),
    path('<int:pk>/transacao/editar/', TransacaoUpdateView.as_view(), name='transacao_editar'),
    path('<int:pk>/transacao/apagar/', TransacaoDeleteView.as_view(), name='transacao_apagar'),
    path('transacao/<int:pk>/', exibir_transacao, name='transacao_exibir'),
]