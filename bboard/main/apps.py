from django.apps import AppConfig
from django.dispatch import Signal

user_registered = Signal()


def user_registered_dispatcher(sender, instance, **kwargs):
    from .utilities import send_activation_notification  # Перенесено сюда

    send_activation_notification(instance)


user_registered.connect(user_registered_dispatcher)


class MainConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'main'
    verbose_name = 'Доска объявлений'
