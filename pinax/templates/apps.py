from django.apps import AppConfig as BaseAppConfig
from django.utils.translation import ugettext_lazy as _


class AppConfig(BaseAppConfig):

    name = "pinax.templates"
    label = "pinax_templates"
    verbose_name = _("Pinax Templates")
