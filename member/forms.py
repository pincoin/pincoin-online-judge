from allauth.account import forms as allauth_forms

from django import forms
from django.utils.translation import ugettext_lazy as _


class MemberLoginForm(allauth_forms.LoginForm):
    class Media:
        js = ('https://www.google.com/recaptcha/api.js',)


class MemberResetPasswordForm(allauth_forms.ResetPasswordForm):
    class Media:
        js = ('https://www.google.com/recaptcha/api.js',)


class MemberResetPasswordKeyForm(allauth_forms.ResetPasswordKeyForm):
    pass


class MemberChangePasswordForm(allauth_forms.ChangePasswordForm):
    pass


class MemberSetPasswordForm(allauth_forms.SetPasswordForm):
    pass


class MemberUnregisterForm(forms.Form):
    agree = forms.BooleanField(
        label=_('I really would like to unregister.'),
    )
