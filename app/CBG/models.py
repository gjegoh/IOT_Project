from django.db import models
from django.contrib.auth.models import User
import uuid

class CBG_Reading(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    Image_ID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Image = models.ImageField(upload_to='Uploaded_Images/CBG_Images/')
    Image_Uploaded_At = models.DateTimeField(blank=True, null=True)