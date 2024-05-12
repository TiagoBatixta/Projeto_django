from django.contrib import admin
from galeria.models import fotografia

class Listfoto(admin.ModelAdmin):
    list_display = ('id', 'nome', 'legenda', "categoria")
    list_display_links = ('id', 'nome')
    search_fields = ('nome', 'id')
    list_filter = ('categoria',)
    list_per_page = 10

admin.site.register(fotografia, Listfoto)

