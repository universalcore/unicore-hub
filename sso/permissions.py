from unicoresso.models import AuthorizedSite
from urlparse import urlparse
import re


def custom_attributes(user, service):
    # e.g
    # User: Joe Soap
    # serice: http://cms.tz.fflangola.qa-hub.unicore.io/login/

    service_domain = urlparse(service).netloc

    sites = [
        s for s in AuthorizedSite.objects.all()
        if re.match(
            re.compile(s.site.replace('.', '\\.').replace('*', '.*')),
            service_domain)]

    if sites:
        user_groups = set(user.groups.values_list('name', flat=True))
        for site in sites:
            site_groups = set(site.group.values_list('name', flat=True))
            intersect = user_groups & site_groups
            if intersect:
                return {
                    'givenName': user.first_name,
                    'email': user.email,
                    'has_perm': True,
                    'service_name': service,
                    'groups': list(intersect)}
    return {
        'givenName': user.first_name,
        'email': user.email,
        'has_perm': False,
        'service_name': service,
        'groups': []}
