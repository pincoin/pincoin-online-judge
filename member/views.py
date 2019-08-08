from allauth.account import views as allauth_views
from django.contrib.auth import mixins as auth_mixins
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


class MemberPasswordChangeView(auth_mixins.LoginRequiredMixin, allauth_views.PasswordChangeView):
    template_name = 'member/account/password_change.html'
    form_class = forms2.MemberChangePasswordForm

    def get_context_data(self, **kwargs):
        context = super(MemberPasswordChangeView, self).get_context_data(**kwargs)
        context['page_title'] = _('Password Change')
        return context


class MemberPasswordSetView(auth_mixins.LoginRequiredMixin, allauth_views.PasswordSetView):
    template_name = 'member/account/password_set.html'
    form_class = forms2.MemberSetPasswordForm

    def get_context_data(self, **kwargs):
        context = super(MemberPasswordSetView, self).get_context_data(**kwargs)
        context['page_title'] = _('Password Set')
        return context


class MemberPasswordReset(allauth_views.PasswordResetView):
    template_name = 'member/account/password_reset.html'
    form_class = forms2.MemberResetPasswordForm

    def get_context_data(self, **kwargs):
        context = super(MemberPasswordReset, self).get_context_data(**kwargs)
        context['page_title'] = _('Password Reset')
        return context


class MemberPasswordResetDoneView(allauth_views.PasswordResetDoneView):
    template_name = 'member/account/password_reset_done.html'

    def get_context_data(self, **kwargs):
        context = super(MemberPasswordResetDoneView, self).get_context_data(**kwargs)
        context['page_title'] = _('Password Reset Done')
        return context


class MemberPasswordResetFromKeyView(allauth_views.PasswordResetFromKeyView):
    template_name = 'member/account/password_reset_from_key.html'
    form_class = forms2.MemberResetPasswordKeyForm

    def get_context_data(self, **kwargs):
        context = super(MemberPasswordResetFromKeyView, self).get_context_data(**kwargs)
        context['page_title'] = _('Password Reset')
        return context


class MemberPasswordResetFromKeyDoneView(allauth_views.PasswordResetFromKeyDoneView):
    template_name = 'member/account/password_reset_from_key_done.html'

    def get_context_data(self, **kwargs):
        context = super(MemberPasswordResetFromKeyDoneView, self).get_context_data(**kwargs)
        context['page_title'] = _('Password Reset Done')
        return context
