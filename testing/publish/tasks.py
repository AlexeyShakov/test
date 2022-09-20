# Create your tasks here
from testing.celery import app
from publish.models import TestSignals
from django.core.mail import send_mail 
from testing.settings import EMAIL_HOST_USER

@app.task
def send_email():
    send_mail(
    "Тема сообщения",
    "Вы получили это сообщение, потому что модель TestSignals была сохранена",
    EMAIL_HOST_USER,
    ['alexei_96@inbox.ru']
    )

