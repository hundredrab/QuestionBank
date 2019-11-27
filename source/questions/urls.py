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
    path('set/<int:pk>/<passcode>',
         views.SetDetail.as_view(),
         name='set_detail'),
    path('set/',
         views.QuestionSetCreate.as_view(),
         name='set_create'),
    path('sets/',
         views.QuestionSetList.as_view(),
         name='set_list'),
    path('<int:pk>/delete',
         views.QuestionDelete.as_view(),
         name='delete_q'),
]
