from django.views.generic.base import TemplateView


class LoginView(TemplateView):
    template_name = "logintest.html"

    def get(self, *args, **kwargs):
        self.request.session['service'] = self.request.GET.get('service')
        return super(LoginView, self).get(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(LoginView, self).get_context_data(*args, **kwargs)
        context.update({'service': self.request.session['service']})
        return context
