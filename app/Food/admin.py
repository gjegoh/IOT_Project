from django.contrib import admin
from .models import Food_Recognition

class Food_RecognitionAdmin(admin.ModelAdmin):
    list_display = (
        "User",
        "Image_ID",
        "Image_Uploaded_At"
    )
    
admin.site.register(Food_Recognition, Food_RecognitionAdmin)