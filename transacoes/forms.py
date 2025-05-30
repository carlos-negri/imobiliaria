from django import forms
from .models import Transacao



class TransacaoModelForm(forms.ModelForm):
    class Meta:
        model = Transacao
        fields = '__all__'

        error_messages = {
            'cliente': {'required': 'O cliente é um campo obrigatório'},
            'imovel': {'required': 'O imóvel é um campo obrigatório'},
            'corretor': {'required': 'O corretor é um campo obrigatório'},
            'proprietario': {'required': 'O proprietário é um campo obrigatório'},
            'tipo': {'required': 'O tipo de transação é um campo obrigatório'},
            'valor': {'required': 'O valor é um campo obrigatório'}
        }


