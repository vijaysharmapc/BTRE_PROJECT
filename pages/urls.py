from django.urls import path
from . import views # from all import views

urlpatterns = [
    path('', views.index, name='index'),  # it empty or root folder
    path('about', views.about, name='about'), # method name is about
]
