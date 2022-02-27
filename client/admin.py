from django.contrib import admin
from .models import Client

# Register your models here.

class Clients(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'cpf', 'rg', 'smartphone', 'active')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'cpf')
    list_filter = ('active',)
    list_editable = ('active',)
    list_per_page = 10
    ordering = ['name']

admin.site.register(Client, Clients)