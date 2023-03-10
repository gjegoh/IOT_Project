from django.urls import path
from . import views

urlpatterns = [
    path('upload_Smart/', views.upload_Smart, name='upload_Smart'),
]