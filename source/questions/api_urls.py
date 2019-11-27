"""
API URLS for question app.
"""

from django.urls import path

from . import api_views as views

app_name = 'questions'

urlpatterns = [
    path('', views.QuestionList.as_view()),
    path('<int:pk>',
         views.QuestionDetail.as_view()),
    path('tags', views.TagList.as_view()),
    path('api/set/<int:pk>',
         views.QuestionSetDetailAPI.as_view(),
         name='question_paper_details'),
    path('add_to_qset/<int:pk>',
         views.AddQuestionToSet.as_view(),
         name='add_to_qset'),
]
