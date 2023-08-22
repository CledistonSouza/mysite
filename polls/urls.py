from django.urls import path
from .views import IndexView, QuestionDetailView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('pergunta/<int:pk>', QuestionDetailView.as_view(), name='question'),
]