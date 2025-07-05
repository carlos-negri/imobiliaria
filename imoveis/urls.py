from django.urls import path
from .views import ImovelView, ImovelUpdateView, ImovelDeleteView, exibir_imovel, ImovelAddEtapa1View, \
    ImovelAddEtapa2View, ImovelDisponivelView

urlpatterns = [
    path('imoveis', ImovelView.as_view(), name='imoveis'),
    path('imoveis/disponiveis/', ImovelDisponivelView.as_view(), name='imoveis_disponiveis'),
    path('imovel/adicionar/', ImovelAddEtapa1View.as_view(), name='imovel_add_etapa1'),
    path('imovel/adicionar/valores/', ImovelAddEtapa2View.as_view(), name='imovel_add_etapa2'),
    path('<int:pk>/imovel/editar/', ImovelUpdateView.as_view(), name='imovel_editar'),
    path('<int:pk>/imovel/apagar/', ImovelDeleteView.as_view(), name='imovel_apagar'),
    path('imovel/<int:pk>/', exibir_imovel, name='imovel_exibir'),
]