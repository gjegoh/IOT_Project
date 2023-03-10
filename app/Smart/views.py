from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.models import User

def upload_Smart(request):
    return render(request, 'Smart/upload_Smart.html')