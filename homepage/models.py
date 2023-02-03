from django.db import models
from django.core import validators
from django.utils import timezone
from django.contrib.auth.models import User


class Categoria(models.Model):
    categoria = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.categoria


class Contato(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING, name='User')
    nome = models.CharField(max_length=150, name='Nome')
    sobrenome = models.CharField(max_length=150, blank=True, name='Sobrenome')
    telefone = models.CharField(
        max_length=11, validators=[
            validators.RegexValidator('^[1-9]{2}?:\d{8}|\d{9}$')
        ],
        name='Telefone'
    )
    email = models.EmailField(
        validators=[validators.validate_email], name='Email'
    )
    data_de_criacao = models.DateTimeField(
        default=timezone.now, name='Data_de_criação'
    )
    descricao = models.TextField(blank=True, name='Descrição')
    categoria = models.ForeignKey(
        Categoria, models.DO_NOTHING, name='Categoria'
    )
    foto = models.ImageField(
        upload_to='img/%Y/%m/%d', blank=True, validators=[
            validators.FileExtensionValidator(['png', 'jpg', 'webp', 'jpeg'])
        ]
    )

    def __str__(self):
        return self.Nome
    
