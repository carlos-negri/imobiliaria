from django import forms
from .models import Imovel

class ImovelModelForm(forms.ModelForm):
    class Meta:
        model = Imovel
        fields = '__all__'
        labels = {
            'codigo_unico': 'Código Único do Imóvel',
            'endereco': 'Endereço Completo',
            'tipo_transacao': 'Tipo de Transação',
            'valor_iptu': 'Valor do IPTU (R$)',
            'valor_condominio': 'Valor do Condomínio (R$)',
            'area_total': 'Área Total (m²)',
            'area_construida': 'Área Construída (m²)',
            'foto_principal': 'Foto Principal do Imóvel',
            'descricao': 'Descrição Detalhada',
            'vagas_garagem': 'Vagas de Garagem',
            'tipo_imovel': 'Tipo de imóvel',
            'status_imovel': 'Situação do imóvel'
        }
        help_texts = {
            'codigo_unico': 'Código único de identificação do imóvel',
            'tipo_transacao': 'Selecione se é venda ou aluguel'
        }

        error_messages = {
        'codigo_unico': {'required': 'O imóvel precisa de um código único', 'unique': 'Imóvel já cadastrado'},
        'endereco': {'required': 'O endereço é um campo obrigatório'},
        'tipo_transacao': {'required': 'O tipo de transação é um campo obrigatório'},
        'valor_iptu':{'required': 'O IPTU é um campo obrigatório'},
        'valor_condominio':{'required': 'O condomínio é um campo obrigatório'},
        'area_total':{'required': 'A área total é um campo obrigatório'},
        'area_construida':{'required': 'A área construída  é um campo obrigatório'},
        'foto':{'required': 'A foto é um campo obrigatório'},
        'descricao':{'required': 'A descrição é um campo obrigatório'},
        'quartos':{'required': 'O número de quartos é um campo obrigatório'},
        'banheiros':{'required': 'O número de banheiros é um campo obrigatório'},
        'vagas_garagem':{'required': 'O número de vagas de garagem é um campo obrigatório'},
        'tipo_imovel':{'required': 'O tipo de imóvel é um campo obrigatório'},
        'status_imovel':{'required': 'O status do imóvel é um campo obrigatório'},
        }