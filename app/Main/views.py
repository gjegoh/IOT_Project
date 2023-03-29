from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import login as login_f, authenticate, logout as logout_f
from django.contrib.auth.forms import AuthenticationForm
from CBG.models import CBG_Food_Record
import datetime
from pytz import timezone

# # endpoint to render index page for all users
# def index(request):
#     if request.method == 'GET':
#         query_set = CBG_Food_Record.objects.all().order_by('Before_CBG_Uploaded_At__minute')
#         readings = []
#         measurements = []
#         foodnames = []
#         cbg_datetime = []
#         for i in query_set:
#             readings.append(i.Before_CBG_Reading)
#             readings.append(i.After_CBG_Reading)
#             measurements.append(i.Before_CBG_Measurement)
#             measurements.append(i.After_CBG_Measurement)
#             foodnames.append(i.Food_Name)
#             cbg_datetime.append(i.Before_CBG_Uploaded_At.astimezone(timezone('Asia/Singapore')).strftime("%Y/%m/%d, %H:%M"))
#             cbg_datetime.append(i.After_CBG_Uploaded_At.astimezone(timezone('Asia/Singapore')).strftime("%Y/%m/%d, %H:%M"))
#         return render(
#             request,
#             'Main/index.html',
#             context={
#                 'readings': readings,
#                 'measurements': measurements,
#                 'foodnames': foodnames,
#                 'cbg_datetime': cbg_datetime
#             }
#         )

# endpoint to render index page for all users
def index(request):
    if request.method == 'GET':
        query_set = CBG_Food_Record.objects.all().order_by('Before_CBG_Uploaded_At__minute')
        results = []
        food = []
        foodlist= []

        for i in query_set:

            each_entry = {
                'Before_CBG_Reading': i.Before_CBG_Reading, 
                'After_CBG_Reading': i.After_CBG_Reading,
                'Before_CBG_Measurement': i.Before_CBG_Measurement,
                'After_CBG_Measurement': i.After_CBG_Measurement,
                'Food_Name': i.Food_Name,
                'Food_Uploaded_At': i.Food_Uploaded_At.astimezone(timezone('Asia/Singapore')).strftime("%Y/%m/%d, %H:%M"),
                'Before_CBG_Uploaded_At': i.Before_CBG_Uploaded_At.astimezone(timezone('Asia/Singapore')).strftime("%Y/%m/%d, %H:%M"),
                'After_CBG_Uploaded_At': i.After_CBG_Uploaded_At.astimezone(timezone('Asia/Singapore')).strftime("%Y/%m/%d, %H:%M")
            }
            results.append(each_entry)


            if i.Food_Name not in foodlist:
                print(i.Food_Name)
                foodlist.append(i.Food_Name)
                each_food = {
                    'Food_Name': i.Food_Name,
                    'Food_Calorie': i.Food_Calorie,
                    'Food_Carb': i.Food_Carb,
                    'Food_Sugar': i.Food_Sugar,
                    'Food_Fibre': i.Food_Fibre
                }
                food.append(each_food)
             
        return render(
            request,
            'Main/index.html',
            context={
                'food': food,
                'results': results
            }
        )

# renders registration page for all users
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login_f(request, user)
            messages.success(request, "Registration successful." )
            return redirect("Main:index")
        else:
            messages.error(request, "Unsuccessful registration.")
    else:
        form = RegistrationForm()
    return render(request, 'Main/register.html', {'form': form})

#  renders login page for all users
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login_f(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("Main:index")
            else:
                messages.error(request,"Invalid username or password.")
        else:
            messages.error(request,"Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, "Main/login.html", context={"form": form})

def logout(request):
	logout_f(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("Main:index")