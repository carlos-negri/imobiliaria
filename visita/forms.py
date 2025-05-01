from django import forms
from .models import Visita
from django.core.exceptions import ValidationError
from datetime import datetime, time, timezone


class VisitaModelForm(forms.ModelForm):
    class Meta:
        model = Visita
        fields = '__all__'
        widgets = {
            'datahora': forms.DateTimeInput(
                attrs={
                    'type':'datetime-local',
                    'class':'form-control',
                    'min': datetime.now().strftime('%Y-%m-%dT%H:%M')
                },
                format='%Y-%m-%dT%H:%M'
            ),
            'observacoes':forms.Textarea(attrs={'rows':3}),
        }
        error_messages = {
            'datahora': {'required': 'A data e hora da visita são obrigatórias', 'invalid':'Informe uma data e hora válidas'},
            'imovel': {'required': 'O código do imóvel é um campo obrigatório'},
            'corretor': {'required': 'O corretor é um campo obrigatório'},
            'cliente': {'required': 'O cliente é um campo obrigatório'},
        }

        def clean_datahora(self):
            datahora = self.cleaned_data.get('datahora')
            if datahora and datahora < datetime.now():
                raise ValidationError("Não é possível agendar visitas para datas/horas passadas")
            return datahora



