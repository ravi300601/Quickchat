from django.apps import AppConfig


class QuickchatConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'quickchatapp'

    def ready(self):
        import quickchatapp.signals
