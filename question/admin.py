from django.contrib import admin
from .models import Tags, Question, Answer, Comment


class QuestionAdmin(admin.ModelAdmin):
    list_display = [
        'user', 'title', 'get_tags', 'views_count', 'created_at'
    ]
    ordering = ('-created_at',)


admin.site.register(Question, QuestionAdmin)
class TagAdmin(admin.ModelAdmin):
    list_display = [
        'tag', 'created_at'
    ]


admin.site.register(Tags, TagAdmin)
admin.site.register(Answer)
admin.site.register(Comment)
