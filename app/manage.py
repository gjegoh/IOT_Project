#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import datetime
from telegram.ext import Updater

def daily_reminder(context):
    context.bot.send_message(chat_id=os.environ.get("CHAT_ID"), text='This is your daily reminder to submit your CBG reading if you have not!   ')

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IOT.settings')
    try:
        from django.core.management import execute_from_command_line

    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

    #Send daily message to the user who's subscribed to DiaBreezyBot
    TOKEN = os.environ.get("TELE_TOKEN")
    updater = Updater(TOKEN, use_context=True)
    job = updater.job_queue
    timeToSendMsg = datetime.time(14, 50, 00, 000000) #24hr clock, uses UTC timing = SG time -8. For example, 10pm SGT = 2pm UTC = 1400H GMT
    job.run_daily(daily_reminder, timeToSendMsg, days=(0, 1, 2, 3, 4, 5, 6), context=None, name=None)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
