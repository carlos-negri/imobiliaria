from django import forms
from .models import Cliente

class ClienteModelForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'

        error_messages = {
            'nome': {'required': 'O nome do cliente é um campo obrigatório'},
            'fone': {'required': 'O telefone do cliente é um campo obrigatório', 'unique': 'Já existe um cliente com esse número de telefone!'},
            'email': {'required': 'O email do cliente é um campo obrigatório', 'unique': 'Já existe um cliente com esse e-mail!'},
        }