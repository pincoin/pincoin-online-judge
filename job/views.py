from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView


class JobListView(TemplateView):
    template_name = "job/job_list.html"

    def get_context_data(self, **kwargs):
        context = super(JobListView, self).get_context_data(**kwargs)
        context['page_title'] = _('Job Openings')
        return context
