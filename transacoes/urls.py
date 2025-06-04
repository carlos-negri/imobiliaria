from django.urls import path
from .views import TransacaoView, TransacaoUpdateView, TransacaoDeleteView, exibir_transacao, TransacaoAddView

urlpatterns = [
    path('transacoes', TransacaoView.as_view(), name='transacoes'),
    path('transacao/adicionar/', TransacaoAddView.as_view(), name='transacao_adicionar'),
    path('<int:pk>/transacao/editar/', TransacaoUpdateView.as_view(), name='transacao_editar'),
    path('<int:pk>/transacao/apagar/', TransacaoDeleteView.as_view(), name='transacao_apagar'),
    path('transacao/<int:pk>/', exibir_transacao, name='transacao_exibir'),
]