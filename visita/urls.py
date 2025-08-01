from django.urls import path
from .views import VisitaView, VisitaAddView, VisitaUpdateView, VisitaDeleteView, VisitaExibir

urlpatterns = [
    path('visitas', VisitaView.as_view(), name='visitas'),
    path('visita/adicionar/', VisitaAddView.as_view(), name='visita_adicionar'),
    path('<int:pk>/visita/editar/', VisitaUpdateView.as_view(), name='visita_editar'),
    path('<int:pk>/visita/apagar/', VisitaDeleteView.as_view(), name='visita_apagar'),
    path('<int:pk>/visita/exibir/', VisitaExibir.as_view(), name='visita_exibir'),
]