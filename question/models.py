from django.db import models
import uuid
from ckeditor.fields import RichTextField
from account.models import Quser


class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True


class Tags(TimeStamp):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    tag = models.CharField(max_length=200, null=True)
    detail = models.TextField(default='', null=True)

    def __str__(self):
        return self.tag

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'
        ordering = ('-id',)


class Question(TimeStamp):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    user = models.ForeignKey(Quser, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=500, null=True)
    tags = models.ManyToManyField(Tags, blank=True)
    detail = RichTextField(blank=True, null=True)
    views_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_tags(self):
        return ",".join([str(p) for p in self.tags.all()])


class Answer(TimeStamp):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    user = models.ForeignKey(Quser, on_delete=models.SET_NULL, null=True)
    question = models.ForeignKey(Question, null=True, on_delete=models.DO_NOTHING)
    answer = models.TextField()
    is_best = models.BooleanField(default=False)
    vote = models.IntegerField(default=0)

    def __str__(self):
        return self.answer


class Comment(TimeStamp):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    user = models.ForeignKey(Quser, on_delete=models.SET_NULL, null=True)
    answer = models.ForeignKey(Answer, null=True, on_delete=models.DO_NOTHING)
    comment = models.TextField()

    def __str__(self):
        return self.comment
