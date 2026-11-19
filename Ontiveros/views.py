from django.shortcuts import render

def inicio (request):
    return render (request, 'Ontiveros/inicio.html')
def registro(request):
    return render(request, 'Ontiveros/formregistro.html')
