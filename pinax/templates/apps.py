from django.apps import AppConfig as BaseAppConfig
from django.utils.translation import gettext_lazy as _


class AppConfig(BaseAppConfig):

    name = "pinax.templates"
    label = "pinax_templates"
    verbose_name = _("Pinax Templates")
