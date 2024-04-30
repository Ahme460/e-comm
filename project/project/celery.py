# celery.py
import os
from celery import Celery

# تعيين الإعدادات الافتراضية لـ 'Django' والتي ستستخدمها عمال Celery.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')

# تحديد التكوين الخاص بـ Celery.
app.config_from_object('django.conf:settings', namespace='CELERY')

# تحميل المهام في التطبيق الخاص بـ Celery.
app.autodiscover_tasks()
