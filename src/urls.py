
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.conf.urls import url
from django.conf import settings 
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('super/admin/', admin.site.urls),
    path('user/', include('account.urls')),
    path('',include('question.urls')),
    path('admin/', include('sadmin.urls')),

    path('home', views.HomeView.as_view(),name ='home')
]
urlpatterns +=  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns +=  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)