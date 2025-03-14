from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now
from datetime import timedelta
from .models import PhishingLog

@receiver(post_save, sender=PhishingLog)
def auto_delete_old_logs(sender, instance, **kwargs):
    days_ago = now() - timedelta(days=1) 
    deleted_count, _ = PhishingLog.objects.filter(timestamp__lt=days_ago).delete()

    if deleted_count > 0:
        print(f"Deleted {deleted_count} old records")