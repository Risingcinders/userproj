from django.shortcuts import render, HttpResponse, redirect
from .models import Dojo, Ninja
import random


def index(request):
    context = {
        "dojos": Dojo.objects.all(),
        "ninjas": Ninja.objects.all()
    }
    return render(request, "rough.html", context)


def dojoadd(request):
    Dojo.objects.create(
        name=request.POST['dojoname'], city=request.POST['dojocity'], state=request.POST['dojostate'])
    return redirect('/nin')


def ninjaadd(request):
    targetdojo = Dojo.objects.get(id=request.POST['dojoid'])
    Ninja.objects.create(dojo_id=targetdojo,first_name=request.POST['first_name'], last_name=request.POST['last_name'])
    return redirect('/nin')

def deletedojo(request, deleteid):
    targetdojo = Dojo.objects.get(id=deleteid)
    targetdojo.delete()
    return redirect('/nin')


