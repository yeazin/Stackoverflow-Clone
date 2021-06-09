
from django.urls import path
from . import views

urlpatterns = [
    path('questions/',views.AllQuestions.as_view(), name='questions'),

    path('tags/', views.AllTags.as_view(), name='tags'),
]