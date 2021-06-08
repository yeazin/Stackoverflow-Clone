from django.contrib import admin
from .models import Tags, Question, Answer, Comment

admin.site.register(Question)
admin.site.register(Tags)
admin.site.register(Answer)
admin.site.register(Comment)
