from django.db import models

class Cliente(models.Model):
    nome = models.CharField('Nome',max_length=100, help_text='Nome completo do cliente')
    fone = models.CharField('Telefone', max_length=15, help_text='Celular completo do cliente')
    email = models.EmailField('Email', help_text='Email completo do cliente')

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome