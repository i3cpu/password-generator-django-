from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.

def index(request):
    return  render(request,'generator/index.html',{'text':'jinja'})

def password(request):
    characters = list('abcdefghijklmnopqrstwxyz')
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTWXYZ'))
    if request.GET.get('numbers'):
        characters.extend(list('1234567890'))
    if request.GET.get('special'):
        characters.extend(list('@#$%^&*()_='))
    length = int(request.GET.get('length',12))

    thepassword  = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return  render(request,'generator/password.html',{'password':thepassword})

def about(request):
    return render(request,'generator/about.html')