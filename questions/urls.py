from django.contrib import admin
from django.urls import path

from .views import QuestionList, QuestionDetail

urlpatterns = [
    path('', QuestionList.as_view()),
    path('<int:pk>', QuestionDetail.as_view()),
]
