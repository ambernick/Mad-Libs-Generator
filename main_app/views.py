from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .models import MadLib
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

class MadLibCreate(LoginRequiredMixin, CreateView):
  model = MadLib
  fields = ['title', 'theme', 'story', 'wordinserts' ]
  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class MadLibUpdate(LoginRequiredMixin, UpdateView):
  model = MadLib
  fields = ['title', 'theme', 'story', 'wordinserts' ]

class MadLibDelete(LoginRequiredMixin, DeleteView):
  model = MadLib
  success_url = '/madlibs/' 

# Define the home view
def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def madlibs_index(request):
  madlibs = MadLib.objects.all()
  return render(request, 'madlibs/index.html', { 'madlibs': madlibs })

@login_required
def madlibs_detail(request, madlib_id):
  madlib = MadLib.objects.get(id=madlib_id)
  return render(request, 'madlibs/detail.html', {
    'madlib': madlib, 
  })

@login_required
def madlibs_generate(request, madlib_id):
  madlib = MadLib.objects.get(id=madlib_id)
  x = madlib.story.rsplit('{}')
  i = 1 
  j = 0
  print(x)
  while i < len(x):
    
    x.insert(i, f"<input type='text' placeholder={ madlib.wordinserts[j] }>") 
    i = i+2 
    j = j+1     
  
  return render(request, 'main_app/madlib_generateform.html', {
    'madlib': madlib, 'madlibArray' : x
  })  