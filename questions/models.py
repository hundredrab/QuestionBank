"""
Models for the question app.
"""
from django.conf import settings
from django.db import models
from django.urls import reverse


class Tag(models.Model):
    """Model for storing tag and related info."""
    name = models.CharField(max_length=30)
    parent = models.ForeignKey('self',
                               related_name='children',
                               on_delete=models.SET_NULL,
                               null=True, blank=True)

    def __str__(self):
        return self.name


class QuestionPaper(models.Model):
    """Model for storing Question paper file and related info."""
    file = models.FileField(upload_to='media/papers',
                            blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              on_delete=models.SET_NULL,
                              null=True, blank=True)
    tag_str = models.TextField(blank=True, null=True)

    def get_absolute_url(self):
        """Returns absolute url of the question paper."""
        return reverse('questions:question_paper_details', args=[self.id])


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
                               related_name='questions',
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
    name = models.CharField(max_length=30, blank=True, null=True,
                            help_text="Enter a name of your choice")
    passcode = models.CharField(max_length=5, blank=True, null=True, 
                                help_text="Use this if you want this to be accesssible to only people who have this passcode.")
    start_time = models.DateTimeField(blank=True, null=True,
                                      help_text="Use this if you want this to be accessible only after a certain time.")
    end_time = models.DateTimeField(blank=True, null=True,
                                    help_text="Use this if you want this set to be accessible only until a certain time.")
    questions = models.ManyToManyField(Question)
    total_marks = models.PositiveIntegerField(default=100)

    def get_absolute_url(self):
        """Returns canonical url or the Question set."""
        return reverse('questions:search_view', args=[self.id])
