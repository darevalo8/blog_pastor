from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def inicio(resquest):
    # debe de tener una varible request que es la de la peticion
    # debe retornar algo ya sea un response o un render

    return HttpResponse("hola mundo")


def bienvenida(resquest):
    # debe de tener una varible request que es la de la peticion
    # debe retornar algo ya sea un response o un render

    return HttpResponse("Te damos la bienvenida")