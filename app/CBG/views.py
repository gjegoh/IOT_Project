from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from CBG.pipelines.CBG_Pipeline import Process_CBG 
import os
from .models import CBG_Image, CBG_Food_Record
from django.views.decorators.csrf import csrf_exempt
from pytz import timezone

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"iot-project-380504-fba837331a02.json"

def upload_CBG(request):
    if request.method == 'POST':
        user = request.user
        CBG_Food_Record.objects.create(
            User=user,
            Before_CBG_Reading=request.POST.get('reading'),
            Before_CBG_Measurement=request.POST.get('measurement'),
            Before_CBG_Uploaded_At=request.POST.get('datetimepicker'),
            Food_Name=request.POST.get('reading7'),
            Food_Calorie=request.POST.get('reading2'),
            Food_Carb=request.POST.get('reading3'),
            Food_Sugar=request.POST.get('reading4'),
            Food_Fibre=request.POST.get('reading5'),
            Food_Uploaded_At=request.POST.get('datetimepicker2'),
            After_CBG_Reading=request.POST.get('reading6'),
            After_CBG_Measurement=request.POST.get('measurement2'),
            After_CBG_Uploaded_At=request.POST.get('datetimepicker3'),
        )
        return HttpResponseRedirect('/')
    else:
        query_set = CBG_Food_Record.objects.all().order_by('Before_CBG_Uploaded_At__minute')
        readings = []
        cbg_datetime = []

        for i in query_set:
            readings.append(i.Before_CBG_Reading)
            readings.append(i.After_CBG_Reading)
            cbg_datetime.append(i.Before_CBG_Uploaded_At.astimezone(timezone('Asia/Singapore')).strftime("%Y/%m/%d, %H:%M"))
            cbg_datetime.append(i.After_CBG_Uploaded_At.astimezone(timezone('Asia/Singapore')).strftime("%Y/%m/%d, %H:%M"))

    return render(request, 'CBG/upload_CBG.html', context={
        'TELE_TOKEN': os.environ.get('TELE_TOKEN'),
        'CHAT_ID': os.environ.get('CHAT_ID'),
        'readings': readings,
        'cbg_datetime': cbg_datetime
    })
    

@csrf_exempt
def read_CBG(request):
    if request.method == 'POST':
        cbg_image = CBG_Image.objects.create(
            Image= request.FILES.get("image")
        )
        cbg_pipeline = Process_CBG()
        reading, measurement = cbg_pipeline.get_Reading(cbg_image.Image.path)
        cbg_image.delete()
        return JsonResponse({
            'reading': reading,
            'measurement': measurement
        })