from django.apps import AppConfig
from django.contrib.auth import get_user_model

from user.monkey_patching import has_profile


class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'user'
    verbose_name = 'User'

    def ready(self):
        UserModel = get_user_model()
        UserModel.add_to_class("has_profile", has_profile)
