from django.apps import AppConfig


class PhishingAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'phishing_app'

    def ready(self):
        import phishing_app.signals
