from __future__ import unicode_literals

from django.db import models
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.

class BaseModel(models.Model):
	nombre = models.CharField(max_length=50)

	class Meta:
		abstract = True

	def __unicode__(self):
		return self.nombre


class Pais(BaseModel):
	pass


class Departamento(BaseModel):
	pais = models.ForeignKey(Pais)


class Ciudad(BaseModel):
	departamento = models.ForeignKey(Departamento)


class Barrio(BaseModel):
	ciudad = models.ForeignKey(Ciudad)


class Persona(BaseModel):
	pais = models.ForeignKey(Pais)
	departamento = ChainedForeignKey(
		Departamento,
		chained_field='pais',
		chained_model_field='pais'
	)
	ciudad = ChainedForeignKey(
		Ciudad,
		chained_field='departamento',
		chained_model_field='departamento'
	)
	barrio = ChainedForeignKey(
		Barrio,
		chained_field='ciudad',
		chained_model_field='ciudad'
	)