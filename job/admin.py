from django.contrib import admin

from . import models


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('title', 'phone', 'fax', 'url')
    search_fields = ('title', 'address')
    ordering = ('-created',)
    readonly_fields = ('is_removed',)


class JobFieldAdmin(admin.ModelAdmin):
    list_display = ('title', 'position')
    ordering = ('position',)


class JobOpeningsAdmin(admin.ModelAdmin):
    list_display = ('title',)

    raw_id_fields = ('company', 'job_field')


admin.site.register(models.Company, CompanyAdmin)
admin.site.register(models.JobField, JobFieldAdmin)
admin.site.register(models.JobOpenings, JobOpeningsAdmin)
