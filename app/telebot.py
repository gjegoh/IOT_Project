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

def daily_reminder(context):
    context.bot.send_message(chat_id=os.environ.get("CHAT_ID"), text=f'<b>This</b> is your daily reminder to submit your CBG reading if you have not!' , parse_mode=ParseMode.HTML)

def daily_report(context):
    data = context.job.context
    today = data['Today']
    allFood = ", ".join(data['FoodList'])
    totalCalories = data['TotalCalories']
    totalCarbs = data['TotalCarbs']
    totalSugar = data['TotalSugar']
    totalFibre = data['TotalFibre']
    allInsight = "\n\n".join(data['Insight'])

    theText = (
        f'<b>Daily Report ({today}) \n Food that you ate today:</b> \n {allFood} \n\n <b>Here are the macros:</b>' 
        f'\n Total Calories: <b>{totalCalories}g</b> \n Total Carbs: <b>{totalCarbs}g</b> \n Total Sugar: <b>{totalSugar}g</b> \n Total Fibre: <b>{totalFibre}g</b>'
        f'\n\n <b>Insights:</b> \n {allInsight}'
        f'\n\n <b>Note:</b> We reference the Type 2 diabetes threshold levels. Over limit(>=8.5mmol/L). Approaching threshold(>=7.5mmol/L). Please drop @ahloysius a telegram message to customise your threshold values'
    )

    context.bot.send_message(chat_id=os.environ.get("CHAT_ID"), text=theText , parse_mode=ParseMode.HTML)

def weekly_report(context):
    context.bot.send_message(chat_id=os.environ.get("CHAT_ID"), text='HAHAHAHA XD')

def main():
    mgTommol = 0.0555
    limit = 8.5 #mmol/L
    query_set = CBG_Food_Record.objects.all().order_by('Before_CBG_Uploaded_At__minute')

    theDict = {
        'Today': "",
        'FoodList': [],
        'TotalCalories': 0,
        'TotalCarbs': 0 ,
        'TotalSugar': 0,
        'TotalFibre': 0,
        'Insight': []
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
                insight += f'Your glucose level is within the <b>normal levels</b>! It is likely fine if you continue consuming this food'

            theDict['Insight'].append(insight)


    TOKEN = os.environ.get("TELE_TOKEN")
    updater = Updater(TOKEN, use_context=True)
    job = updater.job_queue

    timeToSendReport = datetime.time(7, 3, 0, 000000)
    timeToSendMsg = datetime.time(3, 19, 15, 000000) #24hr clock, uses UTC timing = SG time -8. For example, 10pm SGT = 2pm UTC = 1400H GMT

    
    #Code to retrieve data for the past 7 days from DB, sum up values, case statement send if healthy, at risk, unhealthy 
    # job.run_daily(weekly_report, timeToSendReport, days=(0), context=None, name=None)

    #Code to retrieve data for today from DB, reply with list of item consumed along with individual readings
    job.run_daily(daily_report, timeToSendReport, days=(0, 1, 2, 3, 4, 5, 6), context=theDict, name=None)

    job.run_daily(daily_reminder, timeToSendMsg, days=(0, 1, 2, 3, 4, 5, 6), context=None, name=None,) #sun to sat

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

# 1. below / above threshold
# 2. daily report of readings & macros
# 3. weekly report of readings & macros
# 4. take cbg reading reminder