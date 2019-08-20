from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils import Choices
from model_utils.models import (
    TimeStampedModel, SoftDeletableModel
)
from mptt.fields import TreeForeignKey

from conf.models import AbstractCategory


class Category(AbstractCategory):
    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')

    def __str__(self):
        return self.title


class CategoryLanguage(TimeStampedModel):
    category = models.ForeignKey(
        'quest.Category',
        verbose_name=_('Category'),
        db_index=True,
        on_delete=models.CASCADE,
    )

    language = models.CharField(
        max_length=2,
        default='th',
        help_text='th|en|ko|cn|ja',
    )

    description = models.TextField(
        verbose_name=_('Category description'),
    )

    class Meta:
        verbose_name = _('i18n Category')
        verbose_name_plural = _('i18n Categories')


class Problem(SoftDeletableModel, TimeStampedModel):
    STATUS_CHOICES = Choices(
        (0, 'draft', _('Draft')),
        (1, 'published', _('Published')),
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name=_('Author'),
        db_index=True,
        null=True,
        blank=True,
        editable=True,
        on_delete=models.SET_NULL,
        related_name='%(app_label)s_%(class)s_owned',
    )

    title = models.CharField(
        verbose_name=_('Problem title'),
        max_length=255,
    )

    content = models.TextField(
        verbose_name=_('Problem content'),
    )

    input_description = models.TextField(
        verbose_name=_('Input description'),
    )

    output_description = models.TextField(
        verbose_name=_('Output description'),
    )

    sample_input = models.TextField(
        verbose_name=_('Sample input data'),
    )

    sample_output = models.TextField(
        verbose_name=_('Sample output data'),
    )

    time_limit = models.IntegerField(
        verbose_name=_('Time limit'),
        help_text=_('Seconds'),
    )

    memory_limit = models.IntegerField(
        verbose_name=_('Memory limit'),
        help_text=_('MB'),
    )

    level = models.IntegerField(
        verbose_name=_('Level'),
        db_index=True,
    )

    category = TreeForeignKey(
        'quest.Category',
        verbose_name=_('Category'),
        null=True,
        blank=True,
        db_index=True,
        on_delete=models.SET_NULL,
    )

    status = models.IntegerField(
        verbose_name=_('Status'),
        choices=STATUS_CHOICES,
        default=STATUS_CHOICES.draft,
        db_index=True,
    )

    class Meta:
        verbose_name = _('Problem')
        verbose_name_plural = _('Problems')

    def __str__(self):
        return self.title


class TestSet(TimeStampedModel):
    problem = models.ForeignKey(
        'quest.Problem',
        verbose_name=_('Problem'),
        db_index=True,
        on_delete=models.CASCADE,
    )

    input_data = models.TextField(
        verbose_name=_('Input data'),
    )

    output_data = models.TextField(
        verbose_name=_('Output data'),
    )

    position = models.IntegerField(
        verbose_name=_('Position'),
    )

    class Meta:
        verbose_name = _('Test set')
        verbose_name_plural = _('Test sets')

    def __str__(self):
        return self.problem.title
