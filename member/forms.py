from allauth.account import forms as allauth_forms
from django import forms
from django.utils.translation import ugettext_lazy as _

from conf.formmixins import GoogleRecaptchaMixin


class MemberLoginForm(allauth_forms.LoginForm):
    class Media:
        js = ('https://www.google.com/recaptcha/api.js',)


class MemberResetPasswordForm(GoogleRecaptchaMixin, allauth_forms.ResetPasswordForm):
    pass


class MemberResetPasswordKeyForm(allauth_forms.ResetPasswordKeyForm):
    pass


class MemberChangePasswordForm(GoogleRecaptchaMixin, allauth_forms.ChangePasswordForm):
    pass


class MemberSetPasswordForm(GoogleRecaptchaMixin, allauth_forms.SetPasswordForm):
    pass


class MemberUnregisterForm(forms.Form):
    agree = forms.BooleanField(
        label=_('I really would like to unregister.'),
    )


class MemberAddEmailForm(allauth_forms.AddEmailForm):
    pass
