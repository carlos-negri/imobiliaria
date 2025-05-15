from django.urls import path

from imoveis.views import ImovelView
from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('imoveis', ImovelView.as_view(), name='imoveis'),

]