from django.views.generic import RedirectView


class HomeView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'quest:home'
