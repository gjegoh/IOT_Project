from django.contrib import admin
from .models import CBG_Reading

class CBG_ReadingAdmin(admin.ModelAdmin):
    list_display = (
        "User",
        "Image_ID",
        "Image_Uploaded_At"
    )
    
admin.site.register(CBG_Reading, CBG_ReadingAdmin)



