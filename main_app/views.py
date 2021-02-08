from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from .models import MadLib

class MadLibCreate(CreateView):
  model = MadLib
  fields = '__all__'

# Define the home view
def home(request):
  return HttpResponse('<h1>Welcome to Mad Libs Generator(HomePage)!</h1>')

def about(request):
    return render(request, 'about.html')

def madlibs_index(request):
  madlibs = MadLib.objects.all()
  return render(request, 'madlibs/index.html', { 'madlibs': madlibs })