from unicoresso.models import AuthorizedSite
from urlparse import urlparse
import re


def custom_attributes(user, service):
    service_domain = urlparse(service).netloc

    matched_sites = [
        s for s in AuthorizedSite.objects.all()
        if re.match(
            re.compile(s.site.replace('.', '\\.').replace('*', '.*')),
            service_domain)]

    if matched_sites:
        user_groups = set(user.groups.values_list('name', flat=True))
        for site in matched_sites:
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
