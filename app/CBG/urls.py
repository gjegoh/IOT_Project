from django.urls import path
from . import views

urlpatterns = [
    path('upload_CBG/', views.upload_CBG, name='upload_CBG'),
]