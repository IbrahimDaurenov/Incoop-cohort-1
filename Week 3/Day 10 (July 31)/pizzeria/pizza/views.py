from django.shortcuts import render
from django.http import HttpResponse
from .models import *


def index(request):
    context = dict()

    pizzas = Pizza.objects.all()
    countries = Country.objects.all()

    context['pizzas'] = pizzas
    context['countries'] = countries


    return render(request, 'pizza/index.html', context)

def divisors(request, num):
    context = dict()
    num_of_divs = str(len([e for e in range(1,num+1,1) if (num%e==0)]))
    context['num_of_divs'] = num_of_divs
    context['num'] = str(num)
    return render(request, 'pizza/divs.html', context)
