import logging

from django.utils.translation import ugettext_lazy as _
from django.views import generic

from . import models


class JobListView(generic.ListView):
    logger = logging.getLogger(__name__)
    context_object_name = 'jobs'

    template_name = "job/job_list.html"

    def get_queryset(self):
        queryset = models.JobOpenings.objects \
            .select_related('company', 'job_field') \
            .filter(status=models.JobOpenings.STATUS_CHOICES.published)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(JobListView, self).get_context_data(**kwargs)
        context['page_title'] = _('Job Openings')
        return context
