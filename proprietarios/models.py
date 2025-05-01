from django.db import models

class Proprietario(models.Model):
    nome = models.CharField('Nome',max_length=100, help_text='Nome completo do proprietário')
    fone = models.CharField('Telefone', max_length=15, help_text='Celular completo do proprietário')
    email = models.EmailField('Email', help_text='Email completo do proprietário')

    class Meta:
        verbose_name = 'Proprietário'
        verbose_name_plural = 'Proprietários'

    def __str__(self):
        return self.nome