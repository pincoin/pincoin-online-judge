import json
import urllib

from allauth.account import forms as allauth_forms
from django import forms
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


class MemberLoginForm(allauth_forms.LoginForm):
    class Media:
        js = ('https://www.google.com/recaptcha/api.js',)


class MemberResetPasswordForm(allauth_forms.ResetPasswordForm):
    def clean(self):
        cleaned_data = super(MemberResetPasswordForm, self).clean()

        captcha_response = self.data.get('g-recaptcha-response')
        url = 'https://www.google.com/recaptcha/api/siteverify'
        values = {
            'secret': settings.GOOGLE_RECAPTCHA['secret_key'],
            'response': captcha_response
        }
        data = urllib.parse.urlencode(values).encode()
        req = urllib.request.Request(url, data=data)
        captcha_response = urllib.request.urlopen(req)
        result = json.loads(captcha_response.read().decode())

        if not result['success']:
            raise forms.ValidationError(_('Invalid reCAPTCHA. Please try again.'))

        return cleaned_data

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
