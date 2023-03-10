from django.urls import path
from . import views

urlpatterns = [
    path('upload_Food/', views.upload_Food, name='upload_Food'),
]