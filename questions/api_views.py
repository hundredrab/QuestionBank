"""
API Views for the Question app.
"""
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Question, QuestionSet, Tag
from .serializers import (QuestionSerializer, QuestionSetSerializer,
                          TagSerializer)


class QuestionList(generics.ListCreateAPIView):
    """View all questions or create new ones.

    Allowed Methods::

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

    def get_queryset(self):
        queryset = Question.objects.all()
        search_text = self.request.query_params.get('text', None)
        whitelist = self.request.query_params.get('whitelist', None)
        blacklist = self.request.query_params.get('blacklist', None)
        if search_text is not None:
            queryset = queryset.filter(text__contains=search_text)
        if whitelist:
            whitelist = [tag.strip()
                         for tag in whitelist.split(',') if tag.strip()]
            for tag in whitelist:
                queryset = queryset.filter(tags__name=tag)
        if blacklist:
            blacklist = [tag.strip()
                         for tag in blacklist.split(',') if tag.strip()]
            for tag in blacklist:
                queryset = queryset.exclude(tags__name=tag)
        return queryset


class QuestionDetail(generics.RetrieveUpdateAPIView):
    """Get or update a specific question, retrieved by ID."""
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class TagList(generics.ListAPIView):
    """View all tags."""
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class QuestionSetDetailAPI(generics.RetrieveUpdateAPIView):
    """Get or update a specific question, retrieved by ID."""
    serializer_class = QuestionSetSerializer
    queryset = QuestionSet.objects.all()


class AddQuestionToSet(APIView):
    """Add a question to set, as called from the set detail view."""
    def get(self, request, p_key, **kwargs):
        """Handle get method."""
        qset = QuestionSet.objects.get(pk=p_key)
        qpk = self.request.query_params.get('qpk')
        ques = Question.objects.get(pk=qpk)
        qset.questions.add(ques)
        qset.save()
        return Response("Success", 200)
