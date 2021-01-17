from django.forms import ModelForm
from .models import Evento

class EventoForm(ModelForm):
    class Meta:
        model = Evento
        fields = ['codigo', 'cod_relatorio', 'cod_empresa', 'cod_atracao', 'local', 'data','cidade','estado','nome']