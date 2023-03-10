def initial_web_app_group(sender, **kwargs):
    from django.contrib.auth.models import User
    from django.conf import settings
    
    # create superuser if does not exist
    if len(User.objects.filter(username='admin')) == 0:
        User.objects.create_superuser('admin', '', 'admin')
