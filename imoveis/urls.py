from django.urls import path
from .views import ImovelView, ImovelAddView, ImovelUpdateView, ImovelDeleteView, exibir_imovel

urlpatterns = [
    path('imoveis', ImovelView.as_view(), name='imoveis'),
    path('imovel/adicionar/', ImovelAddView.as_view(), name='imovel_adicionar'),
    path('<int:pk>/imovel/editar/', ImovelUpdateView.as_view(), name='imovel_editar'),
    path('<int:pk>/imovel/apagar/', ImovelDeleteView.as_view(), name='imovel_apagar'),
    path('imovel/<int:pk>/', exibir_imovel, name='imovel_exibir'),
]