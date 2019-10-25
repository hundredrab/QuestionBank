from django.db import models
from django.conf import settings

class Tag(models.Model):
    """Model for storing tag and related info."""
    name = models.CharField(max_length=30)
    parent = models.ForeignKey('self',
                               on_delete=models.SET_NULL,
                               null=True, blank=True)

class QuestionPaper(models.Model):
    """Model for storing Question paper file and related info."""
    file = models.FileField(upload_to='papers',
                            blank=True, null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.SET_NULL,
                              null=True, blank=True)

class Question(models.Model):
    """Model for storing each question and related info."""
    text = models.TextField(blank=True, null=True)
    creator = models.ForeignKey(settings.AUTH_USER_MODEL,
                                on_delete=models.SET_NULL,
                                null=True, blank=True)
    notes = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    tags_frozen = models.BooleanField(default=False)
    source = models.ForeignKey(QuestionPaper,
                               blank=True, null=True,
                               on_delete=models.SET_NULL)
    difficulty = models.PositiveIntegerField(blank=True, null=True,
                                             help_text="Marks will be allotted"
                                             "on the basis of this.")
    similar_to = models.ManyToManyField('self', blank=True)

    def __str__(self):
        return self.text[:100]

class QuestionSet(models.Model):
    """QuestionSet for setting questions."""

    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.SET_NULL,
                              null=True, blank=True)
    questions = models.ManyToManyField(Question)
    total_marks = models.PositiveIntegerField(default=100)
