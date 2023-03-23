from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from CBG.pipelines.CBG_Pipeline import Process_CBG 
from .models import CBG_Reading
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"iot-project-380504-fba837331a02.json"

def upload_CBG(request):
    
    if request.method == 'POST':
        submit_type = request.POST.get('submitType')
        user = request.user
        if submit_type == 'image':
            image = request.FILES["fileInput"]
            upload_time = request.POST.get('uploadTime')
            cbg_obj = CBG_Reading.objects.create(
                User=user,
                Image=image,
                Reading_Uploaded_At=upload_time,
            )
            cbg_pipeline = Process_CBG()
            
            reading, measurement = cbg_pipeline.get_Reading(cbg_obj.Image.path)
            CBG_Reading.objects.filter(Reading_ID=cbg_obj.Reading_ID).update(
                Reading=reading,
                Measurement=measurement
            )
        else:
            reading = request.POST.get('reading')
            measurement = request.POST.get('measurement')
            upload_time = request.POST.get('uploadTime1')
            cbg_obj = CBG_Reading.objects.create(
                User=user,
                Reading_Uploaded_At=upload_time,
                Reading=reading,
                Measurement=measurement
            )
        # return render(request, 'CBG/upload_CBG.html')
        return HttpResponseRedirect('/') 
    return render(request, 'CBG/upload_CBG.html', context={
        'TELE_TOKEN': os.environ.get('TELE_TOKEN'),
        'CHAT_ID': os.environ.get('CHAT_ID'),
    })