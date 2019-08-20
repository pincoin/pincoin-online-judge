from django.urls import (
    path
)

from . import views

app_name = 'quest'

urlpatterns = [
    path('problems/',
         views.ProblemListByCategoryView.as_view(), name='problem_list'),
    path('problems/<int:pk>',
         views.ProblemListByCategoryView.as_view(), name='problem_detail'),

    path('level/',
         views.ProblemListByLevelView.as_view(), name='problem_list_by_level'),
    path('category/',
         views.ProblemListByCategoryView.as_view(), name='problem_list_by_category'),

    path('contest/',
         views.ProblemListByCategoryView.as_view(), name='contest_list'),
    path('contest/<int:pk>',
         views.ProblemListByCategoryView.as_view(), name='contest_detail'),

    path('stat/',
         views.ProblemListByCategoryView.as_view(), name='stat_list'),

    path('rank/',
         views.ProblemListByCategoryView.as_view(), name='rank_list'),
]
