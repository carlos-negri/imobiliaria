
from django.db import models
from stdimage import StdImageField


class Corretor(models.Model):
    nome = models.CharField('Nome',max_length=100, help_text='Nome completo do corretor')
    fone = models.CharField('Telefone', max_length=15, help_text='Celular completo do corretor')
    email = models.EmailField('Email', help_text='Email completo do corretor')
    foto = StdImageField('Foto', upload_to='corretores', delete_orphans=True, null=True, blank=True)

    class Meta:
        verbose_name = 'Corretor'
        verbose_name_plural = 'Corretores'

    def __str__(self):
        return self.nome







