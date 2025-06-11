from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import path, reverse_lazy

from imoveis.views import ImovelView
from transacoes.views import TransacaoView
from .views import IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('imoveis', ImovelView.as_view(), name='imoveis'),
    path('imoveis', TransacaoView.as_view(), name='transacoes'),
    path('Login/', LoginView.as_view(template_name='login.html', extra_context={'titulo': 'Autenticacao'}),
         name='login'),
    path('Logout/', LogoutView.as_view(), name='logout', ),
    path('alterar_senha/', PasswordChangeView.as_view(template_name='login.html',
                                                      extra_context={'titulo': 'Alterar senha'},
                                                      success_url=reverse_lazy('index')), name='alterar_senha'),

]