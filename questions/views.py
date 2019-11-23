"""
Web views for the Question app.
"""
import fitz
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.utils.crypto import get_random_string
from django.views import View
from django.views.generic.detail import DetailView

from .forms import QuestionForm
from .models import Question, QuestionPaper, QuestionSet, Tag


class UploadQuestions(LoginRequiredMixin, View):
    """Upload a question paper, and then redirect the user to the page
    associated with the question paper."""
    login_url = '/accounts/login'

    def get(self, request):
        """Handles get method; show user a form to upload papers."""
        form = QuestionForm()
        context = {
            'form': form,
            'papers': QuestionPaper.objects.all(),
        }
        return render(request, 'questions/upload.html', context)

    def post(self, request):
        """Handles post method.

        Redirect user to paper detail page if upload successful.

        Re-render the same page with errors if not."""
        form = QuestionForm(request.POST, request.FILES)
        qpaper = form.save()
        try:
            doc = fitz.open(qpaper.file.path)
            text = ""
            for page in doc.pages():
                text += page.getText()
            qpaper.text = text
            qpaper.save()
            return redirect(qpaper.get_absolute_url())
        except Exception as err:
            form.add_error(None, "Couldn't parse file." + str(err))
            raise
        context = {
            'form': form,
            'papers': QuestionPaper.objects.all(),
        }
        return render(request, 'questions/upload.html', context)


class QuestionPaperDetail(DetailView): # pylint: disable=too-many-ancestors
    """
    Return details for a question paper along with root tag.

    'root' is augmented data for parsing the tag tree.
    """
    model = QuestionPaper

    def get_context_data(self, **kwargs):
        context = super(QuestionPaperDetail, self).get_context_data(**kwargs)
        root = Tag.objects.get(name='root')
        context['root'] = root
        return context


class AddQuestionToPaper(View):
    """Adds a question to a question paper."""

    def post(self, request, p_key):
        """Handle post method.

        Add a question to the database, and assign a paper to it.
        """
        text = request.POST['text']
        difficulty = request.POST.get('difficulty')
        # TODO: Handle difficulty/marks in both form and here
        tags = request.POST.get('tags')
        paper = QuestionPaper.objects.get(pk=p_key)
        paper.tag_str = tags
        paper.save()
        if request.user.is_authenticated:
            user = request.user
        else:
            user = None
        question = Question.objects.create(
            text=text, source=paper, creator=user)
        tags = [i.strip() for i in tags.split(',') if i.strip()]
        for tag in tags:
            tag_obj = Tag.objects.get(name=tag)
            question.tags.add(tag_obj)
        question.save()

        return redirect(paper.get_absolute_url())


class SearchView(LoginRequiredMixin, View):
    """
    View for a question set.

    User can search for questions and add them into the set here.
    """
    def get(self, request, p_key):
        """Handles get method."""
        qset, _ = QuestionSet.objects.get_or_create(pk=p_key, defaults={
            'owner': self.request.user if (
                self.request.user.is_authenticated
            ) else None,
            'passcode': get_random_string(5).upper(),
        })
        root = Tag.objects.get(name='root')
        context = {
            'qset': qset,
            'root': root,
        }
        if qset.owner == self.request.user:
            return render(request, 'questions/index.html', context)
        # TODO: Handle user not having permissions.
        return None
