from django.contrib import admin

from . import models


class CompanyLanguageSetInline(admin.StackedInline):
    model = models.CompanyTranslation
    extra = 1
    fields = ('language', 'title', 'address', 'description')


class JobFieldLanguageSetInline(admin.StackedInline):
    model = models.JobFieldTranslation
    extra = 1
    fields = ('language', 'title')


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('slug', 'phone', 'fax', 'url')
    ordering = ('-created',)
    readonly_fields = ('is_removed',)

    inlines = (CompanyLanguageSetInline,)


class JobFieldAdmin(admin.ModelAdmin):
    list_display = ('slug', 'position')
    ordering = ('position',)

    inlines = (JobFieldLanguageSetInline,)


class JobOpeningsAdmin(admin.ModelAdmin):
    list_display = ('title',)

    raw_id_fields = ('company', 'job_field')


admin.site.register(models.Company, CompanyAdmin)
admin.site.register(models.JobField, JobFieldAdmin)
admin.site.register(models.JobOpenings, JobOpeningsAdmin)
