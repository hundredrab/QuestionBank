from django.contrib import admin
from .models import QuestionPaper, Question, Tag, QuestionSet

admin.site.register(QuestionPaper)
admin.site.register(Question)
admin.site.register(Tag)
admin.site.register(QuestionSet)
