from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from . import models


class TestSetInline(admin.StackedInline):
    model = models.TestSet
    extra = 1
    fields = ('input_data', 'output_data', 'position')
    ordering = ('position',)


class CategoryLanguageSetInline(admin.StackedInline):
    model = models.CategoryTranslation
    extra = 1
    fields = ('language', 'title', 'description')


class ProblemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'level', 'author', 'status', 'created', 'is_removed')
    list_filter = ('status',)
    list_select_related = ('category', 'author')
    search_fields = ('title', 'content')
    date_hierarchy = 'created'

    ordering = ('status', '-created')

    inlines = (TestSetInline,)

    raw_id_fields = ('author',)
    readonly_fields = ('is_removed',)


class CategoryAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title', 'slug')
    list_filter = ('problem__title',)
    mptt_level_indent = 20
    ordering = ('tree_id', 'lft')

    inlines = (CategoryLanguageSetInline,)


admin.site.register(models.Problem, ProblemAdmin)
admin.site.register(models.Category, CategoryAdmin)
