from django.urls import path
from .views import ver_elementos, EventoDetail

urlpatterns = [
    path('sobreEventos/', ver_elementos,name='sobre_eventos'),
    path('evento_detail/<int:pk>/', EventoDetail.as_view(), name='description_event'),

]