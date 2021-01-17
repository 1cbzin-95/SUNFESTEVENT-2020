from django.shortcuts import render
from django.views import View
from eventos.models import Evento
#           ^de outroa aplicação

# Create your views here.

class Home(View):#defino view que erda de View
    def get( self, request, *args, **kwargs):
        lista_eventos = Evento.objects.all()
        return render(request, 'home.html',{'listaEventos':lista_eventos})#criando função com para responder request que vinher com metodo get
        
class SobreNos(View):
    def get( self, request, *args, **kwargs):
        return render(request,'sobrenos.html')