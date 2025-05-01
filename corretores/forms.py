from django import forms
from .models import Corretor

class CorretorModelForm(forms.ModelForm):
    class Meta:
        model = Corretor
        fields = '__all__'

        error_messages = {
            'nome': {'required': 'O nome do cliente é um campo obrigatório'},
            'fone': {'required': 'O telefone do cliente é um campo obrigatório'},
            'email': {'required': 'O email do cliente é um campo obrigatório'},
            'foto': {'required': 'O corretor precisa ter uma foto'}
        }