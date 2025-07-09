from django import forms
from .models import Corretor

class CorretorModelForm(forms.ModelForm):
    class Meta:
        model = Corretor
        fields = '__all__'

        error_messages = {
            'nome': {'required': 'O nome do corretor é um campo obrigatório'},
            'fone': {'required': 'O telefone do corretor é um campo obrigatório', 'unique':'Telefone já cadastrado'},
            'email': {'required': 'O email do corretor é um campo obrigatório', 'unique':'E-mail já cadastrado'},
            'foto': {'required': 'O corretor precisa ter uma foto'}
        }