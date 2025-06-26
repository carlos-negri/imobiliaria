from datetime import datetime
from decimal import Decimal
from django.db import models
import clientes
import corretores
import imoveis
import proprietarios
from visita.models import Visita


class Transacao(models.Model):
    TRANSACAO_CHOICES=[
        ('A', 'Aluguel'),
        ('V', 'Venda'),
    ]

    proprietario = models.ForeignKey(proprietarios.models.Proprietario, verbose_name='Proprietário', help_text='Nome do Proprietário', on_delete=models.CASCADE, related_name='proprietarioTransacao', default='')
    imovel = models.ForeignKey(imoveis.models.Imovel, verbose_name='Imóvel', help_text='Código do Imóvel', on_delete=models.CASCADE, related_name='imovelTransacao', default='')
    cliente = models.ForeignKey(clientes.models.Cliente, verbose_name='Cliente', help_text='Nome do cliente', on_delete=models.CASCADE, related_name='clienteTransacao', default='')
    corretor = models.ForeignKey(corretores.models.Corretor, verbose_name='Corretor', help_text='Nome do corretor', on_delete=models.CASCADE, related_name='corretorTransacao', default='')
    tipo = models.CharField('Tipo de transação', blank=True, choices=TRANSACAO_CHOICES) # Tipo
    valor = models.DecimalField('Valor da transação', max_digits=1000000, decimal_places=2, default=0)



    def save(self, *args, **kwargs):
        visitas = Visita.objects.filter(cliente=self.cliente, imovel=self.imovel)

        for visita in visitas:
            if visita.datahora.date() == datetime.today().date():
                self.valor = (self.valor * Decimal(0.9))
                break
        super().save(*args, **kwargs)

    class Meta:
        unique_together=('imovel', 'cliente', 'tipo')
        verbose_name = 'Imóvel do proprietário'
        verbose_name_plural = 'Imóveis do proprietário'


