from django.apps import AppConfig


class UserFormConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user_form'
    def ready(self):
        import user_form.signals
