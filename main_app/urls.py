from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('madlibs/', views.madlibs_index, name='index'),
    path('madlibs/<int:madlib_id>/', views.madlibs_detail, name='detail'),
    path('madlibsgenerate/<int:madlib_id>/', views.madlibs_generate, name='generate'),
    path('madlibs/create/', views.MadLibCreate.as_view(), name='madlibs_create'),
    path('madlibs/<int:pk>/update/', views.MadLibUpdate.as_view(), name='madlibs_update'),
    path('madlibs/<int:pk>/delete/', views.MadLibDelete.as_view(), name='madlibs_delete'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
]
