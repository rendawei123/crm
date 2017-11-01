from django.apps import AppConfig


class CurdConfig(AppConfig):
    name = 'curd'

    def ready(self):
        from django.utils.module_loading import autodiscover_modules
        autodiscover_modules('curd')
