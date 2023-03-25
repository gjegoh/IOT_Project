from django.db import models
from django.contrib.auth.models import User
import uuid

class CBG_Food_Record(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    Record_ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Before_CBG_Reading = models.FloatField(default=0, blank=True)
    Before_CBG_Measurement = models.CharField(max_length=5, default="",  blank=True)
    Before_CBG_Uploaded_At = models.DateTimeField(blank=True, null=True) 
    Food_Name = models.CharField(max_length=50, default="",  blank=True)
    Food_Calorie = models.FloatField(default=0, blank=True)
    Food_Carb= models.FloatField(default=0, blank=True)
    Food_Sugar= models.FloatField(default=0, blank=True)
    Food_Fibre= models.FloatField(default=0, blank=True)
    Food_Uploaded_At = models.DateTimeField(blank=True, null=True) 
    After_CBG_Reading = models.FloatField(default=0, blank=True)
    After_CBG_Measurement = models.CharField(max_length=5, default="",  blank=True)
    After_CBG_Uploaded_At = models.DateTimeField(blank=True, null=True) 
    
class CBG_Image(models.Model):
    Image_ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Image = models.ImageField(upload_to='CBG_Images/')