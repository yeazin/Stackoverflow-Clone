from django import template
from question.models import Question
import datetime

register = template.Library()


def count_question(value):
    number_of_question = Question.objects.filter(tags__tag=value).count()
    return number_of_question


def count_today_tag_question(value):
    today = datetime.date.today()
    number_of_tag_created_today = Question.objects.filter(tags__tag=value, created_at__date=today).count()
    return number_of_tag_created_today


register.filter('count_question', count_question)
register.filter('count_today_tag_question', count_today_tag_question)
