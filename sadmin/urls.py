from django.urls import path
from django.urls.resolvers import URLPattern
from .views.dashboard import Dashboard

urlpatterns =[
    path('',Dashboard.as_view(),name='dashboard'),
]