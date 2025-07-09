from django.db import models
from django.forms import ImageField
from stdimage import StdImageField
from proprietarios.models import Proprietario

class Imovel (models.Model):
# Tipos de imóvel (usando caixas de seleção)
    TIPO_IMOVEL_CHOICES = [
        ('APTO', 'Apartamento'),
        ('CASA', 'Casa'),
        ('COBERT', 'Cobertura'),
        ('DUPLEX', 'Duplex'),
        ('KITNET', 'Kitnet'),
        ('LOJA', 'Loja'),
        ('PAVIL', 'Pavilhão'),
        ('COMERCIAL', 'Comercial'),
    ]

    # Status do imóvel
    STATUS_CHOICES = [
        ('NOVO', 'Novo'),
        ('USADO', 'Usado'),
        ('PLANTA', 'Planta'),
        ('CONSTR', 'Em construção'),
    ]

    # Campos básicos
    codigo_unico = models.CharField(max_length=50, unique=True)
    endereco = models.CharField(max_length=200)
    tipo_aluguel = models.BooleanField(default=False)
    tipo_venda = models.BooleanField(default=False)
    valor_venda = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    valor_aluguel = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    valor_iptu = models.DecimalField(max_digits=10, decimal_places=2)
    valor_condominio = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    area_total = models.DecimalField(max_digits=10, decimal_places=2)
    area_construida = models.DecimalField(max_digits=10, decimal_places=2)
    foto = StdImageField(upload_to='fotos_imovel', delete_orphans=True, null=True, blank=True)
    descricao = models.TextField(blank=True)
    quartos = models.PositiveIntegerField()
    banheiros = models.PositiveIntegerField()
    vagas_garagem = models.PositiveIntegerField()
    tipo_imovel = models.CharField(max_length=10, choices=TIPO_IMOVEL_CHOICES)
    status_imovel = models.CharField(max_length=10, choices=STATUS_CHOICES)
    proprietarios = models.ManyToManyField(Proprietario, related_name='imoveis', verbose_name='Proprietários')

    # booleanos pras checkboxes
    tem_condominio = models.BooleanField(default=False)
    tem_financiamento = models.BooleanField(default=False)
    tem_mobilia = models.BooleanField(default=False)
    tem_churrasqueira = models.BooleanField(default=False)
    tem_elevador = models.BooleanField(default=False)
    tem_lareira = models.BooleanField(default=False)
    tem_piscina = models.BooleanField(default=False)
    tem_portaria_24h = models.BooleanField(default=False)
    tem_sacada = models.BooleanField(default=False)
    tem_salao_festa = models.BooleanField(default=False)


    def __str__(self):
        return self.codigo_unico


