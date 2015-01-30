from unicoresso.models import authorizedSite
from django.contrib.auth.models import Group, User

def custom_attributes(user, service):
	
	groups = user.groups.values_list('name',flat=True)
	website = authorizedSite.objects.get(site=service) 
	site_groups =  website.group.values_list('name',flat=True)

	if groups and website:
		for group in groups:
			for site_group in site_groups:
				if site_group == group:
					return {'givenName': user.first_name, 'email': user.email, 'has_perm': True, 'service_name': service, 'group': group,}
	return {'givenName': user.first_name, 'email': user.email, 'has_perm': False, 'service_name': service, 'group': groups,}