from django.forms import ModelForm
from .models import QuestionPaper

class QuestionForm(ModelForm):
    class Meta:
        model = QuestionPaper
        fields = ('file',)
