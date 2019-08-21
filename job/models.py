from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils import Choices
from model_utils.models import (
    TimeStampedModel, SoftDeletableModel
)


class Company(SoftDeletableModel, TimeStampedModel):
    title = models.CharField(
        verbose_name=_('Company title'),
        max_length=255,
    )

    address = models.CharField(
        verbose_name=_('Company address'),
        max_length=255,
    )

    number_of_employees_from = models.IntegerField(
        verbose_name=_('Number of employees from'),
        default=1,
    )

    number_of_employees_to = models.IntegerField(
        verbose_name=_('Number of employees to'),
        default=1,
    )

    description = models.TextField(
        verbose_name=_('Company description'),
    )

    phone = models.CharField(
        verbose_name=_('Phone number'),
        max_length=32,
        blank=True,
        null=True,
    )

    fax = models.CharField(
        verbose_name=_('Fax number'),
        max_length=32,
        blank=True,
        null=True,
    )

    url = models.URLField(
        verbose_name=_('URL'),
        max_length=255,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _('Company')
        verbose_name_plural = _('Companies')

    def __str__(self):
        return self.title


class JobField(TimeStampedModel):
    title = models.CharField(
        verbose_name=_('Job field'),
        max_length=255,
    )

    position = models.IntegerField(
        verbose_name=_('Sort order'),
    )

    class Meta:
        verbose_name = _('Job field')
        verbose_name_plural = _('Job fields')

    def __str__(self):
        return self.title


class JobOpenings(TimeStampedModel):
    STATUS_CHOICES = Choices(
        (0, 'draft', _('Draft')),
        (1, 'published', _('Published')),
    )

    LANGUAGE = Choices(
        ('th', _('Thai')),
        ('en', _('English')),
        ('ko', _('Korean')),
        ('cn', _('Chinese')),
        ('ja', _('Japanese')),
    )

    company = models.ForeignKey(
        'job.Company',
        verbose_name=_('Company'),
        db_index=True,
        on_delete=models.CASCADE,
    )

    title = models.CharField(
        verbose_name=_('Job opening title'),
        max_length=255,
    )

    job_field = models.ForeignKey(
        'job.JobField',
        verbose_name=_('Job field'),
        db_index=True,
        on_delete=models.CASCADE,
    )

    description = models.TextField(
        verbose_name=_('Job description'),
    )

    end_date = models.DateField(
        verbose_name=_('End date'),
        null=True,
        blank=True,
    )

    language = models.CharField(
        choices=LANGUAGE,
        max_length=2,
        default=LANGUAGE.th,
    )

    status = models.IntegerField(
        verbose_name=_('Status'),
        choices=STATUS_CHOICES,
        default=STATUS_CHOICES.draft,
        db_index=True,
    )

    class Meta:
        verbose_name = _('Job opening')
        verbose_name_plural = _('Job openings')

    def __str__(self):
        return self.title
