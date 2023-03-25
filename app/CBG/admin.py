from django.contrib import admin
from .models import CBG_Food_Record, CBG_Image

class CBG_Food_RecordAdmin(admin.ModelAdmin):
    list_display = (
        "User",
        "Record_ID"
    )
    
admin.site.register(CBG_Food_Record, CBG_Food_RecordAdmin)

class CBG_ImageAdmin(admin.ModelAdmin):
    list_display = ("Image_ID",)
    
admin.site.register(CBG_Image, CBG_ImageAdmin)



