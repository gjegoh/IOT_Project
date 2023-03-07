from django import forms
from .models import *
from datetime import datetime
from bootstrap_datepicker_plus.widgets import DateTimePickerInput

class CBGForm(forms.ModelForm):
    class Meta:
        model = CBG_Reading
        fields = ['Image', 'Image_Uploaded_At']
        widgets = {
            'Image_Uploaded_At': DateTimePickerInput()
        }
        
        