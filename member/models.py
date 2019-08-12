import uuid

from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils import Choices
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
        verbose_name=_('User status memo'),
        max_length=255,
        blank=True,
    )

    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')

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
        verbose_name = _('Login log')
        verbose_name_plural = _('Login logs')

    def __str__(self):
        return '{} {} {}'.format(self.user.email, self.ip_address, self.created)


class EmailBanned(SoftDeletableModel, TimeStampedModel):
    email = models.EmailField(
        verbose_name=_('Email address'),
    )

    class Meta:
        verbose_name = _('Banned Email Address')
        verbose_name_plural = _('Banned Email Addresses')

    def __str__(self):
        return '{} {}'.format(self.email, self.created)


class Resume(TimeStampedModel):
    STATUS_CHOICES = Choices(
        (0, 'draft', _('Draft')),
        (1, 'published', _('Published')),
    )

    LANGUAGE_CHOICES = Choices(
        (0, 'thai', _('Thai')),
        (1, 'english', _('English')),
        (2, 'chinese', _('Chinese')),
        (3, 'japanese', _('Japanese')),
        (4, 'korean', _('Korean')),
    )

    resume_no = models.UUIDField(
        verbose_name=_('UUID'),
        unique=True,
        default=uuid.uuid4,
        editable=False
    )

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('user'),
        related_name='resumes',
        db_index=True,
        on_delete=models.CASCADE,
    )

    title = models.CharField(
        verbose_name=_('Resume title'),
        max_length=255,
    )

    description = models.TextField(
        verbose_name=_('Resume description'),
    )

    primary = models.BooleanField(
        verbose_name=_('Primary resume'),
        default=False,
        db_index=True,
    )

    status = models.IntegerField(
        verbose_name=_('Status'),
        choices=STATUS_CHOICES,
        default=STATUS_CHOICES.draft,
        db_index=True,
    )

    language = models.IntegerField(
        verbose_name=_('Language'),
        choices=LANGUAGE_CHOICES,
        default=LANGUAGE_CHOICES.thai,
        db_index=True,
    )

    class Meta:
        verbose_name = _('Resume')
        verbose_name_plural = _('Resume')

    def __str__(self):
        return self.title


class ResumeRecord(models.Model):
    resume = models.ForeignKey(
        'member.Resume',
        verbose_name=_('Resume'),
        db_index=True,
        on_delete=models.CASCADE,
    )

    position = models.IntegerField(
        verbose_name=_('Position'),
    )

    class Meta:
        abstract = True


class WorkExperience(ResumeRecord):
    present = models.BooleanField(
        verbose_name=_('Present'),
        default=False,
        db_index=True,
    )

    start_date = models.DateField(
        verbose_name=_('Start date'),
    )

    end_date = models.DateField(
        verbose_name=_('End date'),
        null=True,
        blank=True,
    )

    company = models.CharField(
        verbose_name=_('Company'),
        max_length=255,
    )

    title = models.CharField(
        verbose_name=_('Job title'),
        max_length=255,
    )


class Education(ResumeRecord):
    present = models.BooleanField(
        verbose_name=_('Present'),
        default=False,
        db_index=True,
    )

    start_date = models.DateField(
        verbose_name=_('Start date'),
    )

    end_date = models.DateField(
        verbose_name=_('End date'),
        null=True,
        blank=True,
    )

    school = models.CharField(
        verbose_name=_('School'),
        max_length=255,
    )

    degree = models.CharField(
        verbose_name=_('Degree'),
        max_length=255,
    )

    major = models.CharField(
        verbose_name=_('Major'),
        max_length=255,
    )

    topic = models.TextField(
        verbose_name=_('Research topics'),
    )


'''
class License(ResumeRecord):
    pass


class VolunteerExperience(ResumeRecord):
    pass


class Skill(ResumeRecord):
    pass


class Accomplishment(ResumeRecord):
    pass


class AdditionalInformation(ResumeRecord):
    pass


class SupportedLanguage(ResumeRecord):
    LEVEL_CHOICES = Choices(
        (0, 'beginner', _('Beginner')),
        (1, 'intermediate', _('Intermediate')),
        (2, 'advanced', _('Advanced')),
        (3, 'fluent', _('Fluent')),
    )
'''
