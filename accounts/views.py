from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth import logout

from . import forms
# create your views here
class SignUp( CreateView ):
   form_class = forms.UserCreateForm
   # ---------------------------------------------------------------------------------
   # A note on why it is reverse_lazy and not reverse here
   # At the time of signup when this class is initialised these sentences will be run.
   # At that time we do not want to actually reverse. That is why we use reverse_lazy
   # Just to say that at this time we want to know that when it succeeds to url to go
   # is the name 'accounts:login'.
   # ---------------------------------------------------------------------------------
   success_url = reverse_lazy('accounts:login')
   template_name = 'accounts/signup.html'
