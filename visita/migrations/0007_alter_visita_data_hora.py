# Generated by Django 5.2 on 2025-04-30 23:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visita', '0006_alter_visita_data_hora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visita',
            name='data_hora',
            field=models.DateTimeField(default=datetime.datetime(2025, 4, 30, 20, 56, 47, 368489)),
        ),
    ]
