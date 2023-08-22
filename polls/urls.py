from django.urls import path
from .views import *

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('pergunta/<int:pk>/', QuestionDetailView.as_view(), name='question'),
    path('pergunta/<int:pk>/vote/', vote, name="vote"),
    path('pergunta/<int:pk>/resultado/', ResultsView.as_view(), name='results'),
]