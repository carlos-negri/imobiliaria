from django import forms

from imoveis.models import Imovel
from .models import Transacao

class TransacaoEtapa1Form(forms.ModelForm):
    class Meta:
        model = Transacao
        fields = [
            'tipo',
        ]

        error_messages = {
            'tipo': {'required': 'O tipo de transação é um campo obrigatório'},
        }

class TransacaoEtapa2Form(forms.ModelForm):
    class Meta:
        model = Transacao
        fields = [
            'cliente',
            'proprietario',
            'corretor',
            'imovel',
            'valor'
        ]

        error_messages = {
            'cliente': {'required': 'O cliente é um campo obrigatório'},
            'imovel': {'required': 'O imóvel é um campo obrigatório'},
            'corretor': {'required': 'O corretor é um campo obrigatório'},
            'proprietario': {'required': 'O proprietário é um campo obrigatório'},
            'tipo': {'required': 'O tipo de transação é um campo obrigatório'},
            'valor': {'required': 'O valor é um campo obrigatório'}
        }

    def __init__(self, *args, **kwargs):
        tipo = kwargs.pop('tipo', None)
        super().__init__(*args, **kwargs)
        self.fields['valor'].widget = forms.HiddenInput()

        if tipo == 'V':
            self.fields['imovel'].queryset = Imovel.objects.filter(tipo_venda=True)
        elif tipo == 'A':
            self.fields['imovel'].queryset = Imovel.objects.filter(tipo_aluguel=True)
        else:
            self.fields['imovel'].queryset = Imovel.objects.none()

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


