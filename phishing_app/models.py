from django.db import models

# Create your models here.
class PhishingLog(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} - {self.timestamp}"