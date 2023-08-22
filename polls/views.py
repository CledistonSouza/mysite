from django.views.generic import ListView, DetailView
from .models import *

class IndexView(ListView):
    model = Question
    template_name = "index.html"
    context_object_name = 'questions'

class QuestionDetailView(DetailView):
    model = Question
    template_name = "question.html"




