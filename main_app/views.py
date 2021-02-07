from django.shortcuts import render
from django.http import HttpResponse


class MadLibs:
    def _init_(self, word_descriptions, template):
        self.template = templateself.word_descriptions = word_descriptions 


def get_words_from_user(word_descriptions):
    words = []
    print("Please provide the following words: ")
    for desc in word_descriptions:
        user_input = input(desc + " ")
        words.append(user_input)
    return words
# Define the home view
def home(request):
  return HttpResponse('<h1>Welcome to Mad Libs Generator(HomePage)!</h1>')

def about(request):
    return render(request, 'about.html')

def madlibs_index(request):
    return render(request, 'madlibs/index.html', { 'madlibs' : madlibs } )