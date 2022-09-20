from django.apps import AppConfig


class PublishConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'publish'

    def ready(self):
        from . import singals
    
