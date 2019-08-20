from django.urls import (
    path
)

from . import views

app_name = 'job'

urlpatterns = [
    path('',
         views.JobListView.as_view(), name='job_list'),
]
