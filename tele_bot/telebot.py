import os
import datetime
from telegram.ext import Updater

def daily_reminder(context):
    context.bot.send_message(chat_id=os.environ.get("CHAT_ID"), text='This is your daily reminder to submit your CBG reading if you have not!   ')

def main():
    #Send daily message to the user who's subscribed to DiaBreezyBot
    TOKEN = os.environ.get("TELE_TOKEN")
    updater = Updater(TOKEN, use_context=True)
    job = updater.job_queue
    timeToSendMsg = datetime.time(3, 45, 00, 000000) #24hr clock, uses UTC timing = SG time -8. For example, 10pm SGT = 2pm UTC = 1400H GMT
    job.run_daily(daily_reminder, timeToSendMsg, days=(0, 1, 2, 3, 4, 5, 6), context=None, name=None)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
