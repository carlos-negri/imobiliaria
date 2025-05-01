from django.urls import path
from .views import CorretorView, CorretorAddView, CorretorUpdateView, CorretorDeleteView

urlpatterns = [
    path('corretores', CorretorView.as_view(), name='corretores'),
    path('corretor/adicionar/', CorretorAddView.as_view(), name='corretor_adicionar'),
    path('<int:pk>/corretor/editar/', CorretorUpdateView.as_view(), name='corretor_editar'),
    path('<int:pk>/corretor/apagar/', CorretorDeleteView.as_view(), name='corretor_apagar'),
]