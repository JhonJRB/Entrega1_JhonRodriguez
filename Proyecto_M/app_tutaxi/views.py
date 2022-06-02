from django.http import HttpResponse
from django.shortcuts import render
from app_tutaxi.forms import *
from app_tutaxi.models import * 

# Create your views here.
def inicio(request):
    
    return render(request,'inicio.html')

# *************************Carga de datos ***************************************
def cargar_cliente(request):
    if request.method == "POST":
        cliente1=Cliente_f(request.POST)
        if cliente1.is_valid():
            clientes=cliente1.cleaned_data
            clientes1= Cliente(nombre=clientes['nombre'], apellido=clientes['apellido'],registro=clientes['registro'],movil_asignado=clientes['movil_asignado'])
            clientes1.save()       
            return render(request,'cargar_cliente.html')
    return render(request,'cargar_cliente.html')

def cargar_movil(request):
    if request.method == "POST":
        movil1=Movil_f(request.POST)
        if movil1.is_valid():
            moviles=movil1.cleaned_data
            moviles1= Movil(patente=moviles['patente'], marca=moviles['marca'],modelo=moviles['modelo'],chofer_asignado=moviles['chofer_asignado'])
            moviles1.save()       
            return render(request,'cargar_movil.html')
    return render(request,'cargar_movil.html')
   

def cargar_chofer(request):
    if request.method == "POST":
        chofer1=Chofer_f(request.POST)
        if chofer1.is_valid():
            choferes=chofer1.cleaned_data
            choferes1= Chofer(nombre=choferes['nombre'], apellido=choferes['apellido'],nacimiento=choferes['nacimiento'],movil_a_cargo=choferes['movil_a_cargo'])
            choferes1.save()       
            return render(request,'cargar_chofer.html')
    return render(request,'cargar_chofer.html')

# *******************Visualizacion de datos ****************************************
def ver_chofer(request):
    choferes=Chofer.objects.all()
    dicc={"chofer":choferes}
    return render(request,'ver_chofer.html', dicc)
    
def ver_cliente(request):
    clientes=Cliente.objects.all()
    dicc={"cliente":clientes}
    return render(request,'ver_cliente.html', dicc)

def ver_movil(request):
    moviles=Movil.objects.all()
    dicc={"movil":moviles}
    return render(request,'ver_movil.html', dicc)

#**********************Busquedad de datos ****************************************
def buscar_chofer(request):
    return render(request,'buscar_chofer.html')

def traer_chofer(request):
    if request.POST['nombre_chofer']:
        nombre1=request.POST['nombre_chofer']
        chofer_1= Chofer.objects.filter(nombre__icontains=nombre1)
        dicc={"chofer":chofer_1}
        return render(request,'ver_chofer.html',dicc)
    return render(request,'buscar_chofer.html')
