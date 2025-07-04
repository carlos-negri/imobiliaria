from django import forms

from .models import Imovel

class ImovelEtapa1Form(forms.ModelForm):
    class Meta:
        model = Imovel
        fields = [
            'codigo_unico',
            'endereco',
            'tipo_venda',
            'tipo_aluguel',
        ]

        labels = {
            'codigo_unico': 'Código Único do Imóvel',
            'endereco': 'Endereço Completo',
            'tipo_venda': 'Quero vender',
            'tipo_aluguel': 'Quero alugar',
        }

        help_texts = {
            'codigo_unico': 'Código único de identificação do imóvel',
        }

        error_messages = {
            'codigo_unico': {
                'required': 'O imóvel precisa de um código único',
                'unique': 'Imóvel já cadastrado'
            },
            'endereco': {
                'required': 'O endereço é um campo obrigatório'
            },
        }

    def clean(self):
            cleaned_data = super().clean()
            tipo_venda = cleaned_data.get('tipo_venda')
            tipo_aluguel = cleaned_data.get('tipo_aluguel')

            if not tipo_venda and not tipo_aluguel:
                raise forms.ValidationError(
                    "Você deve selecionar pelo menos uma opção: venda ou aluguel."
                )

            return cleaned_data

class ImovelEtapa2Form(forms.ModelForm):
    tem_condominio = forms.BooleanField(label='Condomínio incluído?', required=False)
    tem_financiamento = forms.BooleanField(label='Aceita financiamento?', required=False)
    tem_mobilia = forms.BooleanField(label='Possui mobília?', required=False)
    tem_churrasqueira = forms.BooleanField(label='Tem churrasqueira?', required=False)
    tem_elevador = forms.BooleanField(label='Possui elevador?', required=False)
    tem_lareira = forms.BooleanField(label='Com lareira?', required=False)
    tem_piscina = forms.BooleanField(label='Tem piscina?', required=False)
    tem_portaria_24h = forms.BooleanField(label='Portaria 24h?', required=False)
    tem_sacada = forms.BooleanField(label='Tem sacada?', required=False)
    tem_salao_festa = forms.BooleanField(label='Tem salão de festas?', required=False)
    class Meta:
        model = Imovel
        fields = [
            'valor_venda',
            'valor_aluguel',
            'valor_iptu',
            'valor_condominio',
            'area_total',
            'area_construida',
            'foto',
            'descricao',
            'quartos',
            'banheiros',
            'vagas_garagem',
            'tipo_imovel',
            'status_imovel',
            'tem_condominio',
            'tem_financiamento',
            'tem_mobilia',
            'tem_churrasqueira',
            'tem_elevador',
            'tem_lareira',
            'tem_piscina',
            'tem_portaria_24h',
            'tem_sacada',
            'tem_salao_festa',
        ]

        labels = {
            'valor_iptu': 'Valor do IPTU (R$)',
            'valor_venda': 'Valor total da venda (R$)',
            'valor_aluguel': 'Valor mensal do aluguel (R$)',
            'valor_condominio': 'Valor do Condomínio (R$)',
            'area_total': 'Área Total (m²)',
            'area_construida': 'Área Construída (m²)',
            'foto': 'Foto Principal do Imóvel',
            'descricao': 'Descrição Detalhada',
            'vagas_garagem': 'Vagas de Garagem',
            'tipo_imovel': 'Tipo de imóvel',
            'status_imovel': 'Situação do imóvel',
        }

        error_messages = {
            'valor_iptu': {'required': 'O IPTU é um campo obrigatório'},
            'valor_condominio': {'required': 'O condomínio é um campo obrigatório'},
            'area_total': {'required': 'A área total é um campo obrigatório'},
            'area_construida': {'required': 'A área construída  é um campo obrigatório'},
            'foto': {'required': 'A foto é um campo obrigatório'},
            'descricao': {'required': 'A descrição é um campo obrigatório'},
            'quartos': {'required': 'O número de quartos é um campo obrigatório'},
            'banheiros': {'required': 'O número de banheiros é um campo obrigatório'},
            'vagas_garagem': {'required': 'O número de vagas de garagem é um campo obrigatório'},
            'tipo_imovel': {'required': 'O tipo de imóvel é um campo obrigatório'},
            'status_imovel': {'required': 'O status do imóvel é um campo obrigatório'},
        }

class ImovelModelForm(forms.ModelForm):
    tem_condominio = forms.BooleanField(label='Condomínio incluído?', required=False)
    tem_financiamento = forms.BooleanField(label='Aceita financiamento?', required=False)
    tem_mobilia = forms.BooleanField(label='Possui mobília?', required=False)
    tem_churrasqueira = forms.BooleanField(label='Tem churrasqueira?', required=False)
    tem_elevador = forms.BooleanField(label='Possui elevador?', required=False)
    tem_lareira = forms.BooleanField(label='Com lareira?', required=False)
    tem_piscina = forms.BooleanField(label='Tem piscina?', required=False)
    tem_portaria_24h = forms.BooleanField(label='Portaria 24h?', required=False)
    tem_sacada = forms.BooleanField(label='Tem sacada?', required=False)
    tem_salao_festa = forms.BooleanField(label='Tem salão de festas?', required=False)
    class Meta:
        model = Imovel
        fields = [
            'codigo_unico',
            'endereco',
            'valor_iptu',
            'valor_condominio',
            'valor_venda',
            'valor_aluguel',
            'area_total',
            'area_construida',
            'foto',
            'descricao',
            'quartos',
            'banheiros',
            'vagas_garagem',
            'tipo_imovel',
            'status_imovel',
            'tem_condominio',
            'tem_financiamento',
            'tem_mobilia',
            'tem_churrasqueira',
            'tem_elevador',
            'tem_lareira',
            'tem_piscina',
            'tem_portaria_24h',
            'tem_sacada',
            'tem_salao_festa',
        ]

        labels = {
            'codigo_unico': 'Código Único do Imóvel',
            'endereco': 'Endereço Completo',
            'valor_iptu': 'Valor do IPTU (R$)',
            'valor_condominio': 'Valor do Condomínio (R$)',
            'valor_venda': 'Valor de Venda (R$)',
            'valor_aluguel': 'Valor de Aluguel (R$)',
            'area_total': 'Área Total (m²)',
            'area_construida': 'Área Construída (m²)',
            'foto': 'Foto Principal do Imóvel',
            'descricao': 'Descrição Detalhada',
            'quartos': 'Quartos',
            'banheiros': 'Banheiros',
            'vagas_garagem': 'Vagas de Garagem',
            'tipo_imovel': 'Tipo de imóvel',
            'status_imovel': 'Situação do imóvel',
        }

        help_texts = {
            'codigo_unico': 'Código único de identificação do imóvel',
        }

        error_messages = {
            'codigo_unico': {
                'required': 'O imóvel precisa de um código único',
                'unique': 'Imóvel já cadastrado'
            },
            'endereco': {'required': 'O endereço é um campo obrigatório'},
            'valor_iptu': {'required': 'O IPTU é um campo obrigatório'},
            'valor_condominio': {'required': 'O condomínio é um campo obrigatório'},
            'area_total': {'required': 'A área total é um campo obrigatório'},
            'area_construida': {'required': 'A área construída  é um campo obrigatório'},
            'foto': {'required': 'A foto é um campo obrigatório'},
            'descricao': {'required': 'A descrição é um campo obrigatório'},
            'quartos': {'required': 'O número de quartos é um campo obrigatório'},
            'banheiros': {'required': 'O número de banheiros é um campo obrigatório'},
            'vagas_garagem': {'required': 'O número de vagas de garagem é um campo obrigatório'},
            'tipo_imovel': {'required': 'O tipo de imóvel é um campo obrigatório'},
            'status_imovel': {'required': 'O status do imóvel é um campo obrigatório'},
        }



