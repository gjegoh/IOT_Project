from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path('', include(('CBG.urls', 'CBG'), namespace='CBG')),
    path('', include(('Main.urls', 'Main'), namespace='Main'))
]
