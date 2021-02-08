from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, DeleteView
from .models import MadLib

class MadLibCreate(CreateView):
  model = MadLib
  fields = '__all__'
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class MadLibDelete(DeleteView):
  model = MadLib
  success_url = '/madlibs/' 

# Define the home view
def home(request):
  return HttpResponse('<h1>Welcome to Mad Libs Generator(HomePage)!</h1>')

def about(request):
    return render(request, 'about.html')

def madlibs_index(request):
  madlibs = MadLib.objects.all()
  return render(request, 'madlibs/index.html', { 'madlibs': madlibs })

def madlibs_detail(request, madlib_id):
  madlib = MadLib.objects.get(id=madlib_id)
  # instantiate FeedingForm to be rendered in the template
  return render(request, 'madlibs/detail.html', {
    # pass the madlib and feeding_form as context
    'madlib': madlib, 
  })