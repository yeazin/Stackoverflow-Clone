
from django.urls import path
from . import views

urlpatterns = [
    path('questions/',views.AllQuestions.as_view(), name='questions'),
    path('question/view/<str:id>', views.SingleQuestion.as_view(), name='single_question'),

    path('tags/', views.AllTags.as_view(), name='tags'),
    path('upvote_tem/', views.upvote_template, name="upvote_tem"),
    path('upvote/', views.upvote, name="upvote")
]
