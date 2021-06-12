from .models import Tags, Question, Answer
from django.db.models import Count


def GlobalVariable(request):
    tags_obj = Tags.objects.all() \
                   .annotate(q_count=Count('question')) \
                   .filter(question__isnull=False) \
                   .order_by('-q_count')[:5]
    question_count = Question.objects.count()
    answer_highest = Question.objects.all() \
                         .annotate(ans_count=Count('answer')) \
                         .filter(answer__isnull=True) \
                         .order_by('-ans_count')[:10]
    answer = Answer.objects.all()
    context = {
        'tag': tags_obj,
        'question_count': question_count,
        'answer_high': answer,
    }
    return context
