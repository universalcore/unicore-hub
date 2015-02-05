from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(
        r'^$',
        login_required(
            TemplateView.as_view(template_name='home.html')),
        name='home'
    ),
    url(r'', include('mama_cas.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
)
