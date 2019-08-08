from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('email', 'full_name')
    search_fields = ('user__email',)
    readonly_fields = ('user', 'full_name', 'email', 'status_memo')
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
        return super(ProfileAdmin, self).get_queryset(request) \
            .select_related('user')


admin.site.register(Profile, ProfileAdmin)
