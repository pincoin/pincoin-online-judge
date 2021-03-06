from django import template
from django.contrib.gis.geoip2 import GeoIP2
from geoip2.errors import AddressNotFoundError

from ..models import LoginLog

register = template.Library()


@register.simple_tag
def get_login_logs(user, count):
    logs = LoginLog.objects.filter(user=user).order_by('-created')[:count]

    for log in logs:
        log.country_code = None
        try:
            if log.ip_address not in ['127.0.0.1']:
                country = GeoIP2().country(log.ip_address)
                log.country_code = country['country_code'].lower()
        except AddressNotFoundError:
            pass

    return logs
