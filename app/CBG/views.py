from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from .forms import *

# endpoint to render index page for all users
def index(request):
    if request.method == 'GET':
        return render(
            request,
            'CBG/index.html'
        )

# renders registration page for all users
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

def upload_CBG(request):
    if request.method == 'POST':
        form = CBGForm(request.POST, request.FILES)
        if form.is_valid():
            cbg_object = form.save(commit=False)
            cbg_object.User = request.user
            cbg_object.save()
            return render(request, 'CBG/upload_CBG.html', {'form': form})
    else:
        form = CBGForm()
    return render(request, 'CBG/upload_CBG.html', {'form': form})