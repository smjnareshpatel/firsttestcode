import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proj.settings')

app = Celery('proj')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()



# https://tekshinobi.com/django-celery-rabbitmq-redis-broker-results-backend/

# https://www.google.com/search?q=rabbitmq+and+redis+together+django&ei=L6vFYY2YE5Wr5OUPubOO-A4&ved=0ahUKEwjN68r6pvz0AhWVFbkGHbmZA-8Q4dUDCA4&uact=5&oq=rabbitmq+and+redis+together+django&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEM0COgcIABBHELADOgYIABAWEB46CAghEBYQHRAeOgUIIRCgAToHCCEQChCgAUoECEEYAEoECEYYAFCQAVicGmD0HGgBcAJ4AIABsQKIAcUMkgEFMi02LjGYAQCgAQHIAQjAAQE&sclient=gws-wiz

# https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html