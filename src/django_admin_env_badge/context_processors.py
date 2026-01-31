from django.conf import settings
from django.http import HttpRequest


def env_badge(request: HttpRequest):
    return {
        "ADMIN_ENV_NAME": getattr(settings, "ADMIN_ENV_NAME", None),
        "ADMIN_ENV_COLOR": getattr(settings, "ADMIN_ENV_COLOR", "#22FE00"),
        'ADMIN_ENV_ICON': getattr(settings, 'ADMIN_ENV_ICON', ''), 
    }
