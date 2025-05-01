from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from imobiliaria import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('visita.urls')),
    path('', include('clientes.urls')),
    path('', include ('proprietarios.urls')),
    path('', include('corretores.urls')),
    path('', include('imoveis.urls'))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)