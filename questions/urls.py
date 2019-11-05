from django.contrib import admin
from django.urls import path

from . import views

app_name = 'questions'

urlpatterns = [
    path('', views.QuestionList.as_view()),
    path('<int:pk>', views.QuestionDetail.as_view()),
    path('paper/<int:pk>', views.QuestionPaperDetail.as_view()),
    path('tags', views.TagList.as_view()),
    path('tag', views.TagTreeView.as_view()),
    path('upload', views.UploadQuestions.as_view()),
    path('api/set/<int:pk>',
         views.QuestionSetDetailAPI.as_view(), name='question_paper_details'),
    path('paper/details/<int:pk>',
         views.QuestionPaperDetail.as_view(), name='question_paper_details'),
    path('paper/<int:pk>/add', views.AddQuestionToPaper.as_view(),
         name='add_question_to_paper'),
    path('search/<int:pk>', views.SearchView.as_view(), name='search_view'),
]
