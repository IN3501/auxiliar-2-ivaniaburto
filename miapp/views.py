from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'miapp/index.html')
def integrantes(request):
    return render(request, 'miapp/integrantes.html')
def cursos(request):
    return render(request, 'miapp/cursos.html')
