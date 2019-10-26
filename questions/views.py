from django.shortcuts import render
from rest_framework import generics

from .models import Question, QuestionPaper
from .serializers import QuestionSerializer


class QuestionList(generics.ListCreateAPIView):
    """View all questions or create new ones.

    Allowed Methods:

     - GET : Get all questions with details.

     - POST : Add a new question. Request format:

            {
                "id": 1,
                "text": "Whoop",
                "notes": "hello world",
                "tags_frozen": false,
                "difficulty": 21,
                "creator": null,
                "source": null,
                "tags": [],
                "similar_to": []
            }
     """
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

class QuestionDetail(generics.RetrieveUpdateAPIView):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()
