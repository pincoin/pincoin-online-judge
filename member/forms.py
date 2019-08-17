from allauth.account import forms as allauth_forms
from django import forms
from django.utils.timezone import (
    now, timedelta
)
from django.utils.translation import ugettext_lazy as _

from conf.formmixins import GoogleRecaptchaMixin
from . import models
from . import settings as member_settings


class MemberLoginForm(GoogleRecaptchaMixin, allauth_forms.LoginForm):
    def __init__(self, *args, **kwargs):
        self.recaptcha = kwargs.pop('recaptcha', None)
        super(MemberLoginForm, self).__init__(*args, **kwargs)

    def clean(self):
        if not self.recaptcha \
                and self.user and self.user.last_login \
                and now() - self.user.last_login > timedelta(days=member_settings.DAYS_LOGIN_RECPATCHA):
            raise forms.ValidationError(_("You haven't logged for {} days.")
                                        .format(member_settings.DAYS_LOGIN_RECPATCHA))

        if self.recaptcha:
            self.validate_google_recaptcha()

        cleaned_data = super(MemberLoginForm, self).clean()
        return cleaned_data


class MemberResetPasswordForm(GoogleRecaptchaMixin, allauth_forms.ResetPasswordForm):
    def clean(self):
        self.validate_google_recaptcha()

        cleaned_data = super(MemberResetPasswordForm, self).clean()
        return cleaned_data


class MemberResetPasswordKeyForm(allauth_forms.ResetPasswordKeyForm):
    pass


class MemberChangePasswordForm(GoogleRecaptchaMixin, allauth_forms.ChangePasswordForm):
    def clean(self):
        self.validate_google_recaptcha()

        cleaned_data = super(MemberChangePasswordForm, self).clean()
        return cleaned_data


class MemberSetPasswordForm(GoogleRecaptchaMixin, allauth_forms.SetPasswordForm):
    def clean(self):
        self.validate_google_recaptcha()

        cleaned_data = super(MemberSetPasswordForm, self).clean()
        return cleaned_data


class MemberUnregisterForm(forms.Form):
    agree = forms.BooleanField(
        label=_('I really would like to unregister.'),
    )


class MemberAddEmailForm(allauth_forms.AddEmailForm):
    pass


class ResumeForm(forms.Form):
    title = forms.CharField(
        label=_('Resume title'),
        max_length=255,
    )

    description = forms.CharField(
        label=_('Resume description'),
        widget=forms.Textarea(attrs={"rows": 5, "cols": 20}),
    )

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)

        super(ResumeForm, self).__init__(*args, **kwargs)

    def clean(self):
        if models.Resume.objects.filter(user__pk=self.request.user.id).count() > member_settings.NUMBER_OF_RESUME:
            raise forms.ValidationError(_('You cannot have more than {} resumes.'
                                          .format(member_settings.NUMBER_OF_RESUME)))


class ResumeDeleteForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        self.resume_uuid = kwargs.pop('resume_uuid', None)

        super(ResumeDeleteForm, self).__init__(*args, **kwargs)

    def clean(self):
        self.cleaned_data['resume'] = models.Resume.objects \
            .get(user__pk=self.request.user.id,
                 resume_uuid=self.resume_uuid)

        if not self.cleaned_data['resume']:
            raise forms.ValidationError(_('Resume does not exist.'))
