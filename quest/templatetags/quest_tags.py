from django import template

from .. import models

register = template.Library()


@register.simple_tag
def get_categories(language='th'):
    categories = models.Category.objects \
        .filter(children__isnull=True) \
        .order_by('tree_id', 'lft')

    return categories
