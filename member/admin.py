from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from . import models


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name')
    search_fields = ('user__email',)
    readonly_fields = ('user', 'full_name', 'email', 'status_memo')
    raw_id_fields = ('user',)
    ordering = ['-created']

    fieldsets = (
        (_('Account'), {
            'fields': ('user', 'full_name', 'email')
        }),
        (_('Profile'), {
            'fields': ('status_memo',)
        }),
    )

    def get_queryset(self, request):
        return super(ProfileAdmin, self) \
            .get_queryset(request) \
            .select_related('user')


class ResumeAdmin(admin.ModelAdmin):
    pass


class LoginLogAdmin(admin.ModelAdmin):
    list_display = (
        'full_name', 'user', 'ip_address', 'created'
    )
    list_select_related = ('user', 'user__profile')
    readonly_fields = ('user', 'ip_address')
    search_fields = ('user__email', 'ip_address')
    ordering = ['-created']

    def get_queryset(self, request):
        return super(LoginLogAdmin, self).get_queryset(request) \
            .select_related('user', 'user__profile') \
            .filter(user__profile__isnull=False)

    def full_name(self, instance):
        return '{} / {}'.format(instance.user.profile.full_name, instance.user.email)

    full_name.short_description = _('Full name')


class EmailBannedAdmin(admin.ModelAdmin):
    list_display = (
        'email', 'created',
    )
    search_fields = ('email',)
    readonly_fields = ('is_removed', 'created')
    ordering = ['-created']


admin.site.register(models.Profile, ProfileAdmin)
admin.site.register(models.Resume, ResumeAdmin)
admin.site.register(models.LoginLog, LoginLogAdmin)
admin.site.register(models.EmailBanned, EmailBannedAdmin)
