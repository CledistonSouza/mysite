from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.generic import ListView, DetailView
from .models import *

class IndexView(ListView):
    model = Question
    template_name = "index.html"
    context_object_name = 'questions'

class QuestionDetailView(DetailView):
    model = Question
    template_name = "question.html"

class ResultsView(DetailView):
    model = Question
    template_name = "results.html"

def vote(request, pk):
    question = get_object_or_404(Question, pk=pk)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("results", args=(question.id,)))


