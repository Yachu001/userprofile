from django.shortcuts import render,redirect
from .models import userprofile
from django.views.generic import ListView,DetailView



class list_userprofile(ListView):
    model=userprofile
    template_name='userlist.html'
    context_object_name = 'userlists'
    
class detail_userprofile(DetailView):
    model=userprofile
    template_name='userdetail.html'
    context_object_name = 'userlists'
