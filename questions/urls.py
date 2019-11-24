"""
Web URLS for question app.
"""

from django.urls import path

from . import views

app_name = 'questions'

urlpatterns = [
    path('paper/<int:pk>',
         views.QuestionPaperDetail.as_view()),
    path('upload',
         views.UploadQuestions.as_view(),
         name='upload'),
    path('paper/details/<int:pk>',
         views.QuestionPaperDetail.as_view(),
         name='question_paper_details'),
    path('paper/<int:pk>/add',
         views.AddQuestionToPaper.as_view(),
         name='add_question_to_paper'),
    path('search/<int:pk>',
         views.SearchView.as_view(),
         name='search_view'),
    path('set/',
         views.QuestionSetCreate.as_view(),
         name='set_create'),
]
