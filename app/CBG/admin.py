from django.contrib import admin
from .models import CBG_Reading

class CBG_ReadingAdmin(admin.ModelAdmin):
    list_display = (
        "User",
        "Reading_ID",
        "Reading",
        "Measurement"
    )
    
admin.site.register(CBG_Reading, CBG_ReadingAdmin)



