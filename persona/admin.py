from django.contrib import admin
from .models import Pais, Departamento, Ciudad, Barrio, Persona
# Register your models here.


@admin.register(Pais)
class PaisAdmin(admin.ModelAdmin):
	list_display =['id', 'nombre']


@admin.register(Departamento)
class DepartamentoAdmin(admin.ModelAdmin):
	list_display = ['id', 'nombre', 'pais']


@admin.register(Barrio)
class BarrioAdmin(admin.ModelAdmin):
	list_display = ['id', 'nombre', 'ciudad']


@admin.register(Ciudad)
class CiudadAdmin(admin.ModelAdmin):
	list_display = ['id', 'nombre', 'departamento']


@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
	list_display = ['id', 'nombre', 'pais', 'departamento', 'ciudad']

