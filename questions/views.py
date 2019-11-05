import fitz
from django.shortcuts import redirect, render
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from rest_framework import generics

from .forms import QuestionForm
from .models import Question, QuestionPaper, Tag
from .serializers import (QuestionPaperSerializer, QuestionSerializer,
                          TagSerializer, TagTree)


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
    def get_queryset(self):
        queryset = Question.objects.all()
        search_text = self.request.query_params.get('text', None)
        # tag = self.request.query_params.get('tag', None)
        if search_text is not None:
            queryset = queryset.filter(text__contains=search_text)
        # if tag is not None:
            # queryset = queryset.filter(tag_id=tag)
        return queryset


class QuestionDetail(generics.RetrieveUpdateAPIView):
    """Get or update a specific question, retrieved by ID."""
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class TagList(generics.ListAPIView):
    """View all tags."""
    serializer_class = TagSerializer
    queryset = Tag.objects.all()


class TagTreeView(generics.ListAPIView):
    """"""
    serializer_class = TagTree
    queryset = Tag.objects.filter(name='science')


class UploadQuestions(View):
    """Upload a question paper, and then redirect the user to the page
    associated with the question paper."""
    def get(self, request):
        form = QuestionForm()
        context = {
            'form': form,
            'papers': QuestionPaper.objects.all(),
        }
        return render(request, 'questions/upload.html', context)

    def post(self, request):
        form = QuestionForm(request.POST, request.FILES)
        qp = form.save()
        try:
            # TODO: Convert to text and save()
            print(qp.file.path)
            doc = fitz.open(qp.file.path)
            text = ""
            for page in doc.pages():
                text += page.getText()
            qp.text = text
            qp.save()
            return redirect(qp.get_absolute_url())
        except Exception as e:
            form.add_error(None, "Couldn't parse file." + str(e))
            raise
        context = {
            'form': form,
            'papers': QuestionPaper.objects.all(),
        }
        return render(request, 'questions/upload.html', context)

class QuestionPaperDetail(DetailView):
    model = QuestionPaper


class QuestionPaperDetailAPI(generics.RetrieveUpdateAPIView):
    """Get or update a specific question, retrieved by ID."""
    serializer_class = QuestionPaperSerializer
    queryset = QuestionPaper.objects.all()


class AddQuestionToPaper(View):
    """Adds a question to a question paper."""
    def post(self, request, pk):
        text = request.POST['text']
        print(text)
        paper = QuestionPaper.objects.get(pk=pk)
        if request.user.is_authenticated:
            user = request.user
        else:
            user = None
        Question.objects.create(text=text, source=paper, creator=user)
        return redirect(paper.get_absolute_url())


class SearchView(View):
    def get(self, request, pk):
        return render(request, 'questions/index.html')
