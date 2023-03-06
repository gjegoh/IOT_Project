def initial_web_app_group(sender, **kwargs):
    from django.contrib.auth.models import User
    from django.conf import settings
    
    # create mock django user accounts
    if len(User.objects.filter(username='admin')) == 0:
        User.objects.create_superuser('admin', '', 'admin')
