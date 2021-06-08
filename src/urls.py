
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('account.urls')),
    path('question/',include('question.urls')),

    path('', views.HomeView.as_view(),name ='home')
]
