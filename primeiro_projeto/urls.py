from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# Rotas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls'))
]

# Conf de URL dos arquivos estáticos

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
