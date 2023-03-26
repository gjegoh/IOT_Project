import os
import datetime
from telegram.ext import Updater
from telegram import ParseMode

def daily_reminder(context):
    context.bot.send_message(chat_id=os.environ.get("CHAT_ID"), text='<b>This</b> is your daily reminder to submit your CBG reading if you have not!', parse_mode=ParseMode.HTML)

def daily_report(context):
    context.bot.send_message(chat_id=os.environ.get("CHAT_ID"), text='HAHAHAHA DAILY REPORT XD')

def weekly_report(context):
    context.bot.send_message(chat_id=os.environ.get("CHAT_ID"), text='HAHAHAHA XD')

def main():
    #Send daily message to the user who's subscribed to DiaBreezyBot
    TOKEN = os.environ.get("TELE_TOKEN")
    updater = Updater(TOKEN, use_context=True)
    job = updater.job_queue

    timeToSendMsg = datetime.time(10, 49, 00, 000000) #24hr clock, uses UTC timing = SG time -8. For example, 10pm SGT = 2pm UTC = 1400H GMT
    timeToSendReport = datetime.time(23, 59, 00, 000000)
    
    #Code to retrieve data for the past 7 days from DB, sum up values, case statement send if healthy, at risk, unhealthy 
    # job.run_daily(weekly_report, timeToSendReport, days=(0), context=None, name=None)

    #Code to retrieve data for today from DB, reply with list of item consumed along with individual readings
    job.run_daily(daily_report, timeToSendReport, days=(0, 1, 2, 3, 4, 5, 6), context=None, name=None)

    job.run_daily(daily_reminder, timeToSendMsg, days=(0, 1, 2, 3, 4, 5, 6), context=None, name=None) #sun to sat

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

# 1. below / above threshold
# 2. daily report of readings & macros
# 3. weekly report of readings & macros
# 4. take cbg reading reminder