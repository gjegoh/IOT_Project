#!/usr/bin/env python
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IOT.settings')
import django
django.setup()
import datetime
from datetime import datetime as dt
from telegram.ext import Updater
from telegram import ParseMode
from CBG.models import CBG_Food_Record
from random import randrange

def daily_reminder(context):
    context.bot.send_message(chat_id=os.environ.get("CHAT_ID"), text=f'This is your daily reminder to <b>submit your CBG reading</b> if you have not!' , parse_mode=ParseMode.HTML)

def daily_report(context):
    data = context.job.context
    today = data['Today']
    allFood = ", ".join(data['FoodList'])
    totalCalories = data['TotalCalories']
    totalCarbs = data['TotalCarbs']
    totalSugar = data['TotalSugar']
    totalFibre = data['TotalFibre']
    allInsight = "\n\n".join(data['Insight'])
    tip = data['Tip']

    theText = (
        f'<b>Daily Report ({today})\nFood that you ate today:</b> \n {allFood} \n\n <b>Nutrients values:</b>' 
        f'\nTotal Calories: <b>{totalCalories}kcal</b> \nTotal Carbs: <b>{totalCarbs}g</b> \nTotal Sugar: <b>{totalSugar}g</b> \nTotal Fibre: <b>{totalFibre}g</b>'
        f'\n\n<b>Insights:</b> \n{allInsight}'
        f'\n\nTip of the day: {tip}'
        f'\n\n<b>Note:</b> We reference the Type 2 diabetes threshold levels. Over limit(>=8.5mmol/L). Approaching threshold(>=7.5mmol/L). Please drop @ahloysius a telegram message to customise your threshold values'
    )

    context.bot.send_message(chat_id=os.environ.get("CHAT_ID"), text=theText , parse_mode=ParseMode.HTML)

def weekly_report(context):
    context.bot.send_message(chat_id=os.environ.get("CHAT_ID"), text='HAHAHAHA XD')

def main():
    mgTommol = 0.0555
    limit = 8.5 #mmol/L
    query_set = CBG_Food_Record.objects.all().order_by('Before_CBG_Uploaded_At__minute')
    tipBank = ["<b>Choose healthier carbohydrates!</b>It’s important to cut down on foods low in fibre such as white bread, white rice and highly-processed cereals. Choose healthier food like unsweetened milk, brown rice, or pulses like chickpeas",
                "<b>Cut down on added sugar!</b>We know cutting out sugar can be really hard at the beginning, so small practical swaps are a good starting point when you’re trying to cut down on excess sugar. Swapping sugary drinks, energy drinks and fruit juices with water, plain milk, or tea and coffee without sugar can be a good start",
                "<b>Don’t bother with so-called diabetic food! There isn’t any evidence that these foods offer you a special benefit over eating healthily. They can also often contain just as much fat and calories as similar products, and can still affect your blood glucose level. These foods can also sometimes have a laxative effect.</b>",
                "<b>Be smart with snacks!</b>If you want a snack, choose yoghurts, unsalted nuts, seeds, fruits and vegetables instead of crisps, chips, biscuits and chocolates. But watch your portions still – it’ll help you keep an eye on your weight",
                "<b>Eat less salt!Eating lots of salt can increase your risk of high blood pressure, which in turn increases risk of heart diseases and stroke. And when you have diabetes, you’re already more at risk of all of these conditions. Try to limit yourself to a maximum of 6g (one teaspoonful) of salt a day.</b>"]

    theDict = {
        'Today': "",
        'FoodList': [],
        'TotalCalories': 0,
        'TotalCarbs': 0,
        'TotalSugar': 0,
        'TotalFibre': 0,
        'Insight': [],
        'Tip': ""
    }

    for i in query_set:
        before = i.Before_CBG_Reading
        after = i.After_CBG_Reading
        if i.Before_CBG_Measurement == 'mgdL':
            before *= mgTommol

        if i.After_CBG_Measurement == 'mgdL':
            after *= mgTommol       

        today = dt.today().strftime('%Y-%m-%d')
        if str(i.After_CBG_Uploaded_At.date()) == today:
            theDict['Today'] = today
            theDict['FoodList'].append(i.Food_Name)
            theDict['TotalCalories'] += i.Food_Calorie
            theDict['TotalCarbs'] += i.Food_Carb
            theDict['TotalSugar'] += i.Food_Sugar
            theDict['TotalFibre'] += i.Food_Fibre
            insight = f'<b>{i.Food_Name}</b> ({"{:.1f}".format(after)} mmol/L) - '   

            if after > limit:
                insight += f'This food spiked your glucose level <b>over the limit</b>. Try not to consume this food too often'
            elif after > (limit - 1):
                insight += f'Your glucose level <b>reached near the threshold limit</b> after consuming this food item. You might want to monitor the consumption'
            else:
                insight += f'Your glucose level is within <b>normal levels</b>! It is likely fine if you continue consuming this food'

            theDict['Insight'].append(insight)

    theDict['Tip'] = tipBank[randrange(4)]
    TOKEN = os.environ.get("TELE_TOKEN")
    updater = Updater(TOKEN, use_context=True)
    job = updater.job_queue

    timeToSendReport = datetime.time(12, 30, 0, 000000)
    timeToSendMsg = datetime.time(12, 30, 15, 000000) #24hr clock, uses UTC timing = SG time -8. For example, 10pm SGT = 2pm UTC = 1400H GMT

    
    #Code to retrieve data for the past 7 days from DB, sum up values, case statement send if healthy, at risk, unhealthy 
    # job.run_daily(weekly_report, timeToSendReport, days=(0), context=None, name=None)

    #Code to retrieve data for today from DB, reply with list of item consumed along with individual readings
    job.run_daily(daily_report, timeToSendReport, days=(0, 1, 2, 3, 4, 5, 6), context=theDict, name=None)

    job.run_daily(daily_reminder, timeToSendMsg, days=(0, 1, 2, 3, 4, 5, 6), context=None, name=None,) #sun to sat

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()