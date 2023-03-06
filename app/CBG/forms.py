from django import forms
from .models import *
from datetime import datetime

class CBGForm(forms.ModelForm):
    class Meta:
        model = CBG_Reading
        fields = ['Image', 'Image_Uploaded_At']
        widgets = {
            'Image_Uploaded_At': forms.widgets.DateInput(attrs={'type': 'date', 'value': datetime.now().strftime('%Y-%m-%d')})
        }
        
        