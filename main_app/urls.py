from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('madlibs/', views.madlibs_index, name='index'),
    path('madlibs/<int:madlib_id>/', views.madlibs_detail, name='detail'),
    path('madlibs/create/', views.MadLibCreate.as_view(), name='madlibs_create')
]
