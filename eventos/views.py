from django.contrib.auth.decorators import login_required #conf.login
from django.shortcuts import render
from .models import Evento
from django.views.generic.detail import DetailView  

# Create your views here.
@login_required
def ver_elementos(request):
    return render(request,'sobre_eventos.html')

#@login_required <---- não funciona em class
class EventoDetail(DetailView):
    model = Evento