
from django.urls import path
from .import views

urlpatterns = [
    path('dashboard/',views.Dashboard.as_view(), name='dashboard'),

    path('register/', views.Register.as_view(), name='register'),
    path('login/', views.LoginView.as_view(),name='login'),
    path('logout/', views.LogoutView.as_view(), name="logout"),

    path('question/ask',views.CreateQuestion.as_view(),name='ask'),
]