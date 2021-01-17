from django.contrib import admin
from django.urls import path, include
from home import urls as home_urls
from eventos import urls as eventos_urls

# !1 para o django moder servir arquivos estaticos durante o desenvolvimento
from  django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(home_urls)),
    path('eventos/',include(eventos_urls)),
    path('accounts/',include('django.contrib.auth.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
