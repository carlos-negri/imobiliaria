from django.db import models
from corretores.models import Pessoa


class Proprietario(Pessoa):

    class Meta:
        verbose_name = 'Proprietário'
        verbose_name_plural = 'Proprietários'

    def __str__(self):
        return self.nome

class ImoveisProprietario(models.Model):
    imovel = models.ForeignKey('imoveis.Imovel', verbose_name='Imovel', help_text='Imóvel',
                                on_delete=models.CASCADE, related_name='imovelprop')
    proprietario = models.ForeignKey('proprietarios.Proprietario', verbose_name='Proprietario', help_text='Nome do proprietario',
                                on_delete=models.CASCADE, related_name='proprietarioimov')
    class Meta:
        unique_together=('proprietario', 'imovel')
        verbose_name = 'Imóvel do proprietário'
        verbose_name_plural = 'Imóveis do proprietário'

    def unique_error_message(self, model_class, unique_check): #esse metodo sobrescreve o do django pra tratar essa minha excecao
        if model_class == type(self) and unique_check == ('proprietario', 'imovel'):
            return 'Esse imóvel já está associado a esse proprietário'
        else:
            return super(ImoveisProprietario, self).unique_error_message(model_class, unique_check)


    def __str__(self):
        return f'{self.imovel}'