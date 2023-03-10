from django import forms
from .models import *
from datetime import datetime
from bootstrap_datepicker_plus.widgets import DateTimePickerInput

class FoodForm(forms.ModelForm):
    class Meta:
        model = Food_Recognition
        fields = ['Image', 'Image_Uploaded_At']
        widgets = {
            'Image_Uploaded_At': DateTimePickerInput()
        }
        
        