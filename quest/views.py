from django.utils.translation import ugettext_lazy as _
from django.views.generic import TemplateView


class ProblemListByLevelView(TemplateView):
    template_name = "quest/problem_list_by_level.html"

    def get_context_data(self, **kwargs):
        context = super(ProblemListByLevelView, self).get_context_data(**kwargs)
        context['page_title'] = _('Problems By Level')
        return context


class ProblemListByCategoryView(TemplateView):
    template_name = "quest/problem_list_by_category.html"

    def get_context_data(self, **kwargs):
        context = super(ProblemListByCategoryView, self).get_context_data(**kwargs)
        context['page_title'] = _('Problems By Category')
        return context
