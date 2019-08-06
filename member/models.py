from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import (
    TimeStampedModel, SoftDeletableModel
)


class Profile(TimeStampedModel):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )

    organization = models.CharField(
        verbose_name=_('Organization'),
        max_length=255,
        blank=True,
    )

    status_memo = models.CharField(
        verbose_name=_('user status memo'),
        max_length=255,
        blank=True,
    )

    class Meta:
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')

    def __str__(self):
        return '{} profile - user {}/{}'.format(self.id, self.user.id, self.user.username)

    @property
    def full_name(self):
        return '{} {}'.format(self.user.first_name, self.user.last_name)

    full_name.fget.short_description = _('Full name')

    @property
    def email(self):
        return self.user.email

    email.fget.short_description = _('E-mail')


class LoginLog(TimeStampedModel):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('user'),
        null=True,
        blank=True,
        editable=True,
        on_delete=models.SET_NULL,
        related_name="%(app_label)s_%(class)s_owned",
    )

    ip_address = models.GenericIPAddressField(
        verbose_name=_('IP address'),
    )

    class Meta:
        verbose_name = _('login log')
        verbose_name_plural = _('login logs')

    def __str__(self):
        return '{} {} {}'.format(self.user.email, self.ip_address, self.created)


class EmailBanned(SoftDeletableModel, TimeStampedModel):
    email = models.EmailField(
        verbose_name=_('email address'),
    )

    class Meta:
        verbose_name = _('Banned Email Address')
        verbose_name_plural = _('Banned Email Addresses')

    def __str__(self):
        return '{} {}'.format(self.email, self.created)


class PhoneBanned(SoftDeletableModel, TimeStampedModel):
    phone = models.CharField(
        verbose_name=_('phone number'),
        max_length=16,
        default='01012341234',
    )

    class Meta:
        verbose_name = _('Banned Phone Number')
        verbose_name_plural = _('Banned Phone Numbers')

    def __str__(self):
        return '{} {}'.format(self.phone, self.created)
