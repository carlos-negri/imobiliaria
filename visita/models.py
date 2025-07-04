from datetime import datetime
from django.db import models


import clientes.models
import corretores.models
import imoveis.models

data= datetime.now()

class Visita(models.Model):
    SITUACAO_CHOICES=[
        ('A', 'Agendada'),
        ('CA', 'Cancelada'),
        ('CO', 'Concluída'),
    ]


    cliente = models.ForeignKey(clientes.models.Cliente, verbose_name='Cliente', help_text='Nome do cliente', on_delete=models.CASCADE, related_name='cliente', default='')  # Linka ao cliente
    corretor = models.ForeignKey(corretores.models.Corretor, verbose_name='Corretor', help_text='Nome do corretor', on_delete=models.CASCADE, related_name='corretor', default='')  # Linka ao corretor
    imovel = models.ForeignKey(imoveis.models.Imovel, verbose_name='Imóvel', help_text='Código Único do Imóvel', on_delete=models.CASCADE, related_name='imovel', default='')
    datahora = models.DateTimeField(verbose_name='Data e Hora da visita')  # Data e hora da visita
    observacoes = models.TextField(blank=True)  # Campo opcional
    situacao = models.CharField('Situação da visita', max_length=100, blank=True, choices=SITUACAO_CHOICES, default='A') # Situação

    def __str__(self):
        return f"Visita no imóvel {self.imovel}. Cliente:  {self.cliente}. Corretor: {self.corretor} | Situação: {self.situacao} | Data: {self.datahora}"