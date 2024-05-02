from django.shortcuts import render
from django.http import HttpResponse



def index(request):
    
    dados = {
    1: {"nome": "Nebulosa", 
        "legenda": "webbtelescope.org/ NASA / James Webb Space"},
    2: {"nome": "Galaxia NGC",
        "legenda": "nasa.org/ NASA / Hubble & NASA / J. Lee e A. Filippenko"}
    }    
    return render(request, "galeria/index.html", {"cards": dados})

def imagem(request):
    return render(request, "galeria/imagem.html")