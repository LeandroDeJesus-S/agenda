from django.contrib import admin
from .models import Categoria, Contato


class ContatoAdmin(admin.ModelAdmin):
    list_display = [
        'User', 'Nome', 'Sobrenome', 'Telefone', 'Categoria'
    ]
    ordering = ['Nome']
    search_fields = [
        'Nome', 'Sobrenome', 'Telefone'
    ]
    list_filter = ['Categoria']

admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
