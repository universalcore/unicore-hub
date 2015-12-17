from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from sso import views
from mama_cas.views import LoginView

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^accounts/login/?$',
        views.LoginView.as_view(),
        name='login'
        ),
    url(r'^accounts/login-cas/?$', LoginView.as_view(), name='cas_login'),
    url(r'^social/', include('social.apps.django_app.urls',
                             namespace='social')),
    url(r'accounts/', include('mama_cas.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^grappelli/', include('grappelli.urls')),
    url(
        r'^$',
        login_required(
            TemplateView.as_view(template_name='home.html')),
        name='home'),
)
