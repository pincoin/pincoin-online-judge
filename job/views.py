import logging

from django.utils.translation import ugettext_lazy as _
from django.views import generic

from . import forms
from . import models


class JobListView(generic.ListView):
    logger = logging.getLogger(__name__)
    context_object_name = 'jobs'
    form_class = forms.JobSearchForm

    template_name = "job/job_list.html"

    def get_queryset(self):
        form = self.form_class(self.request.GET)

        queryset = models.JobOpenings.objects \
            .select_related('company', 'job_field') \
            .filter(status=models.JobOpenings.STATUS_CHOICES.published)

        return queryset

    def get_context_data(self, **kwargs):
        context = super(JobListView, self).get_context_data(**kwargs)
        context['page_title'] = _('Job Openings')
        context['form'] = self.form_class(
            tech_stack=self.request.GET.get('tech_stack') if self.request.GET.get('tech_stack') else '',
            company=self.request.GET.get('company') if self.request.GET.get('company') else '',
            address=self.request.GET.get('address') if self.request.GET.get('address') else '',
        )
        return context
