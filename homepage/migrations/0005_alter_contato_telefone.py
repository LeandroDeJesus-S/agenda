# Generated by Django 4.1.5 on 2023-01-31 21:00

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_alter_contato_telefone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='Telefone',
            field=models.CharField(max_length=11, validators=[django.core.validators.RegexValidator('^[1-9]{2}?:\\d{8}|\\d{9}$')]),
        ),
    ]
