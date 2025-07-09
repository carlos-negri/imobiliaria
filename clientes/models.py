

from corretores.models import Pessoa


class Cliente(Pessoa):

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.nome