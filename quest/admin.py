from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin

from .models import (
    Problem, TestSet, Category
)


class TableSetInline(admin.StackedInline):
    model = TestSet
    extra = 1
    fields = ('input_data', 'output_data', 'position')
    ordering = ('position',)


class ProblemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'level', 'author', 'status', 'created', 'is_removed')
    list_filter = ('status',)
    list_select_related = ('category', 'author')
    search_fields = ('title', 'content')
    date_hierarchy = 'created'
    inlines = (TableSetInline,)
    ordering = ('status', '-created')

    raw_id_fields = ('author',)
    readonly_fields = ('is_removed',)


class CategoryAdmin(DraggableMPTTAdmin):
    list_display = ('tree_actions', 'indented_title', 'slug')
    list_filter = ('problem__title',)
    prepopulated_fields = {'slug': ('title',)}
    mptt_level_indent = 20
    ordering = ('tree_id', 'lft')


admin.site.register(Problem, ProblemAdmin)
admin.site.register(Category, CategoryAdmin)
