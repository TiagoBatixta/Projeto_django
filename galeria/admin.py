from django.contrib import admin
from galeria.models import fotografia

class Listfoto(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda')
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'id')

admin.site.register(fotografia, Listfoto)

