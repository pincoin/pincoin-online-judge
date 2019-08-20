from django.urls import (
    path
)

from . import views

app_name = 'quest'

urlpatterns = [
    path('problems/level/',
         views.ProblemListByLevelView.as_view(), name='problem_list_by_level'),
    path('problems/category/',
         views.ProblemListByCategoryView.as_view(), name='problem_list_by_category'),
]
