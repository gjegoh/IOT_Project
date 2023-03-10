from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from .forms import *

def upload_Food(request):
    if request.method == 'POST':
        form = FoodForm(request.POST, request.FILES)
        if form.is_valid():
            food_object = form.save(commit=False)
            food_object.User = request.user
            food_object.save()
            return render(request, 'Food/upload_Food.html', {'form': form})
    else:
        form = FoodForm()
    return render(request, 'Food/upload_Food.html', {'form': form})