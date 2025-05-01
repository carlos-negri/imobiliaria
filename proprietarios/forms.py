from django import forms
from .models import Proprietario

class ProprietarioModelForm(forms.ModelForm):
    class Meta:
        model = Proprietario
        fields = '__all__'

        error_messages = {
            'nome': {'required': 'O nome do proprietário é um campo obrigatório'},
            'fone': {'required': 'O telefone do proprietário é um campo obrigatório'},
            'email': {'required': 'O email do proprietário é um campo obrigatório'},
        }