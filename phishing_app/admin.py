from django.contrib import admin
from phishing_app import models

# Register your models here.
class AccountSuperAdmin(admin.ModelAdmin):
    list_display = ["email", "password", "timestamp"]
    list_filter = ["email"]
    search_fields = ["email"]
    list_per_page = 10

admin.site.register(models.PhishingLog, AccountSuperAdmin)
