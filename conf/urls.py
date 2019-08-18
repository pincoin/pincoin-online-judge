from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import (
    path, include
)

from conf.views import HomeView

urlpatterns = [
    path('',
         HomeView.as_view(), name='home'),

    path('{}'.format(settings.ADMIN_URL),
         admin.site.urls),

    path('i18n/',
         include('django.conf.urls.i18n')),

    path('quest/',
         include('quest.urls', namespace='quest')),

    path('accounts/',
         include('member.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
