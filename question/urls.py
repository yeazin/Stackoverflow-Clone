
from django.urls import path
from . import views

urlpatterns = [
    path('create-question/',views.CreateQuestion.as_view(),name='create_question'),
    path('questions/',views.AllQuestions.as_view(), name='questions'),

    path('tags/', views.AllTags.as_view(), name='tags'),
]