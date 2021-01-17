from django.urls import path
from .views import Home, SobreNos

urlpatterns = [
    path('', Home.as_view(),name='home'),
    path('sobrenos/', SobreNos.as_view(),name='sobre_nos'),#as_view() visao baseada em classes
]