from django.contrib import admin
from .models import Tags, Question, Answer, Comment


class QuestionAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'title', 'get_tags', 'views_count', 'created_at'
    ]
    ordering = ('-created_at',)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Tags)
admin.site.register(Answer)
admin.site.register(Comment)
