from django.urls import path

from proprietarios.views import ProprietarioView, ProprietarioAddView, ProprietarioUpdateView, ProprietarioDeleteView

urlpatterns = [
    path('proprietarios', ProprietarioView.as_view(), name='proprietarios'),
    path('proprietario/adicionar/', ProprietarioAddView.as_view(), name='proprietario_adicionar'),
    path('<int:pk>/proprietario/editar/', ProprietarioUpdateView.as_view(), name='proprietario_editar'),
    path('<int:pk>/proprietario/apagar/', ProprietarioDeleteView.as_view(), name='proprietario_apagar'),
]