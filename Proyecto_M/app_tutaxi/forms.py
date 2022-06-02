from django import forms

class Cliente_f(forms.Form):
    nombre= forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    registro=forms.DateField()
    movil_asignado=forms.IntegerField()
    
class Movil_f(forms.Form):
    patente= forms.CharField(max_length=40)
    marca=forms.CharField(max_length=40)
    modelo=forms.DateField()
    chofer_asignado=forms.IntegerField()
    
class Chofer_f(forms.Form):
    nombre= forms.CharField(max_length=40)
    apellido=forms.CharField(max_length=40)
    nacimiento=forms.DateField()
    movil_a_cargo=forms.IntegerField()
    

    
    