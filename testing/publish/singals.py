from django.dispatch import receiver
from django.db.models.signals import post_save
from publish.models import TestSignals
from datetime import datetime

@receiver(post_save, sender=TestSignals)
def post_save_date(sender, instance, created, **kwargs):
    # instance.previous_date = instance.date
    # instance.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sender.objects.filter(id=instance.id).update(previous_date=instance.date, date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))