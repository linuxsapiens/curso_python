from django.shortcuts import render, HttpResponse, redirect
from . import models

# Create your views here.
def hello(request):
    return HttpResponse("Hola mundo loco")

def about(request):
    return HttpResponse("Acerca de ...")

def index(request):
    todoes = models.Todo.objects.all()
    return render(request, 'base.html', {
        'todo_list': todoes
    })

def add(request):
    titulo = request.POST['title']
    print(f"titulo: {titulo}")
    models.Todo.objects.create(title=titulo)
    return redirect('/')

def delete(request, id):
    todo = models.Todo.objects.filter(id=id).first()
    todo.delete()
    return redirect('/')

def update(request, id):
    todo = models.Todo.objects.filter(id=id).first()
    todo.complete = not todo.complete
    todo.save()
    return redirect('/')
