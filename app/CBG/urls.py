from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('upload_CBG/', views.upload_CBG, name='upload_CBG'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)