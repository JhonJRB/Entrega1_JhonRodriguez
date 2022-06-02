from django.db import models

# Create your models here.
class Chofer(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    nacimiento=models.DateField()
    movil_a_cargo=models.IntegerField()
    
class Cliente(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    registro=models.DateField()
    movil_asignado=models.IntegerField()    
    
class Movil(models.Model):
    patente=models.CharField(max_length=40)
    marca=models.CharField(max_length=40)
    modelo=models.DateField()
    chofer_asignado=models.IntegerField()    
    
    
