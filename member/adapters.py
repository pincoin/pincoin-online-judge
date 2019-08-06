from allauth.account.adapter import DefaultAccountAdapter
from django import forms
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from . import settings as member_settings
from .models import EmailBanned


class MyAccountAdapter(DefaultAccountAdapter):
    def send_mail(self, template_prefix, email, context):
        pass

    def clean_email(self, email):
        if email.lower().split('@')[1] in member_settings.DISALLOWED_EMAIL_DOMAIN:
            raise forms.ValidationError(_('Your email domain is not allowed.'))

        if EmailBanned.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(_('Your email is banned.'))

        return email

    def get_login_redirect_url(self, request):
        return reverse('home')
