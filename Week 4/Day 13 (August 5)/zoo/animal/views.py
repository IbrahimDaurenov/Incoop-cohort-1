from django.shortcuts import render, redirect
from .models import *
from .forms import *

def index(request):
    context = dict()
    return render(request, 'animal/index.html', context)

def animals(request):
    context = dict()
    animals = Animal.objects.all()
    context['animals'] = animals
    return render(request, 'animal/animals.html', context)


def types(request):
    context = dict()
    types = Type.objects.all()
    context['types'] = types
    return render(request, 'animal/types.html', context)

def type(request, name):
    context = dict()
    type = Type.objects.get(name = name)
    context['type'] = type


    animals = Animal.objects.filter(type = type)
    context['animals'] = animals


    return render(request, 'animal/type.html', context)


def rooms(request):
    context = dict()
    rooms = Room.objects.all()
    context['rooms'] = rooms
    return render(request, 'animal/rooms.html', context)

def animal(request, key):
    context = dict()
    animal = Animal.objects.get(pk = key)
    context['animal'] = animal

    if (request.method == "POST"):
        author = request.POST['author']
        content = request.POST['content']
        comment = Comment(author = author, content = content)
        comment.save()
        animal.comments.add(comment)
        animal.save()

    return render(request, 'animal/animal.html', context)

def add_type(request):
    context = dict()
    form = AddTypeForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data['name']
            language = form.cleaned_data['language']
            type = Type(name = name, language = language)
            type.save()
            return render(request, 'animal/add_type.html', context)

    else:
        context['form']=form
        return render(request, 'animal/add_type.html', context)



    return render(request, 'animal/add_type.html', context)


# Create your views here.
