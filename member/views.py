from allauth.account import views as allauth_views
from django.utils.translation import ugettext_lazy as _

from . import forms2


class MemberLoginView(allauth_views.LoginView):
    template_name = 'member/account/login.html'
    form_class = forms2.MemberLoginForm

    def get_context_data(self, **kwargs):
        context = super(MemberLoginView, self).get_context_data(**kwargs)
        context['page_title'] = _('Login')
        return context


class MemberLogoutView(allauth_views.LogoutView):
    template_name = 'member/account/logout.html'

    def get_context_data(self, **kwargs):
        context = super(MemberLogoutView, self).get_context_data(**kwargs)
        context['page_title'] = _('Logout')
        return context
