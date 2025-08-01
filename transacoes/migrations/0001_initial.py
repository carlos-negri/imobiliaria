# Generated by Django 5.2 on 2025-07-09 02:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('clientes', '0001_initial'),
        ('corretores', '0001_initial'),
        ('imoveis', '0002_initial'),
        ('proprietarios', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(blank=True, choices=[('A', 'Aluguel'), ('V', 'Venda')], verbose_name='Tipo de transação')),
                ('valor', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Valor da transação')),
                ('comissao', models.DecimalField(decimal_places=2, default=0, max_digits=12, verbose_name='Valor da comissão')),
                ('cliente', models.ForeignKey(default='', help_text='Nome do cliente', on_delete=django.db.models.deletion.CASCADE, related_name='clienteTransacao', to='clientes.cliente', verbose_name='Cliente')),
                ('corretor', models.ForeignKey(default='', help_text='Nome do corretor', on_delete=django.db.models.deletion.CASCADE, related_name='corretorTransacao', to='corretores.corretor', verbose_name='Corretor')),
                ('imovel', models.ForeignKey(default='', help_text='Código do Imóvel', on_delete=django.db.models.deletion.CASCADE, related_name='imovelTransacao', to='imoveis.imovel', verbose_name='Imóvel')),
                ('proprietario', models.ForeignKey(default='', help_text='Nome do Proprietário', on_delete=django.db.models.deletion.CASCADE, related_name='proprietarioTransacao', to='proprietarios.proprietario', verbose_name='Proprietário')),
            ],
            options={
                'verbose_name': 'Imóvel do proprietário',
                'verbose_name_plural': 'Imóveis do proprietário',
                'unique_together': {('imovel', 'cliente')},
            },
        ),
    ]
