from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')
app.config_from_object('django.conf:settings', namespace='CELERY')
# Celery beat settings
app.conf.beat_schedule = {
    'enviar-recordatorios-diarios': {
        'task': 'libros.tasks.enviar_recordatorios',
        'schedule': crontab(minute='*/1'),
    },
}
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
