from django import template

from .. import models

register = template.Library()


@register.simple_tag
def get_categories(language='th'):
    categories = models.CategoryTranslation.objects \
        .select_related('category') \
        .filter(category__children__isnull=True,
                language=language) \
        .order_by('category__tree_id', 'category__lft')

    return categories
