from django import forms
from django.forms import inlineformset_factory


from .models import Proprietario, ImoveisProprietario


class ProprietarioModelForm(forms.ModelForm):
    class Meta:
        model = Proprietario
        fields = '__all__'

        error_messages = {
            'nome': {'required': 'O nome do proprietário é um campo obrigatório'},
            'fone': {'required': 'O telefone do proprietário é um campo obrigatório', 'unique':'Telefone já cadastrado!'},
            'email': {'required': 'O email do proprietário é um campo obrigatório', 'unique': 'E-mail já cadastrado!'},
        }

ImoveisProprietarioInLine = inlineformset_factory(Proprietario, ImoveisProprietario, fk_name='proprietario',
                                              fields=('proprietario', 'imovel'), extra=1, can_delete=True)