from datetime import datetime
from decimal import Decimal
from django.db import models
from django.utils import timezone

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
    valor = models.DecimalField('Valor da transação', max_digits=12, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        visitas = Visita.objects.filter(cliente=self.cliente, imovel=self.imovel)

        for visita in visitas:
            if visita.datahora.date() == timezone.now().date():
                if self.tipo == 'V':
                    self.valor = self.imovel.valor_venda * Decimal('0.9')
                elif self.tipo == 'A':
                    self.valor = self.imovel.valor_aluguel * Decimal('0.9')
                break
        else:
            if self.tipo == 'V':
                self.valor = self.imovel.valor_venda
            elif self.tipo == 'A':
                self.valor = self.imovel.valor_aluguel

        super().save(*args, **kwargs)

    class Meta:
        unique_together=('imovel', 'cliente')
        verbose_name = 'Imóvel do proprietário'
        verbose_name_plural = 'Imóveis do proprietário'

    def unique_error_message(self, model_class, unique_check):
        if unique_check == ('imovel', 'cliente'):
            return 'Este cliente já possui uma transação para este imóvel (aluguel ou venda).'
        return super().unique_error_message(model_class, unique_check)


