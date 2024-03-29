# Generated by Django 4.1.5 on 2023-01-28 13:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_alter_categoria_categoria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='Email',
            field=models.EmailField(max_length=254, validators=[django.core.validators.EmailValidator()]),
        ),
        migrations.AlterField(
            model_name='contato',
            name='Telefone',
            field=models.CharField(max_length=11, validators=[django.core.validators.RegexValidator('^[1-9]{2}\\d{9}$')]),
        ),
    ]
