def initial_web_app_group(sender, **kwargs):
    from django.contrib.auth.models import User
    from django.conf import settings
    from CBG.models import CBG_Food_Record
    import csv
    
    # create superuser if does not exist
    if len(User.objects.filter(username='admin')) == 0:
        User.objects.create_superuser('admin', '', 'admin')

    if not CBG_Food_Record.objects.exists():
        print("###  Importing readings.csv ###")
        admin = User.objects.get(username='admin')
        readings_csv = open("DB_init/readings.csv")
        readings = csv.reader(readings_csv)
        next(readings, None)
        readings_dict = {}
        for reading in readings:
            readings_dict[reading[0]] = CBG_Food_Record.objects.create(User=admin, Before_CBG_Reading=reading[0], Before_CBG_Measurement=reading[1], Before_CBG_Uploaded_At=reading[2], Food_Name=reading[3], Food_Calorie=reading[4], Food_Carb=reading[5], Food_Sugar=reading[6], Food_Fibre=reading[7], Food_Uploaded_At=reading[8], After_CBG_Reading=reading[9], After_CBG_Measurement=reading[10], After_CBG_Uploaded_At=reading[11])