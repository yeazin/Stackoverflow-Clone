from django import template
from question.models import Question
# import datetime
import datetime

# import time
# import calendar

register = template.Library()


def count_question(value):
    number_of_question = Question.objects.filter(tags__tag=value).count()
    return number_of_question


def count_today_tag_question(value):
    today = datetime.date.today()
    number_of_tag_created_today = Question.objects.filter(tags__tag=value, created_at__date=today).count()
    return number_of_tag_created_today


def last_week_tag_question(value):
    today = datetime.date.today()
    year, week, day_of_week = today.isocalendar()
    first_day = first_day_of_week(year, week)
    question_count = Question.objects.filter(tags__tag=value, created_at__date__gte=first_day,
                                             created_at__date__lte=today).count()
    return question_count


# helper function
def first_day_of_week(year, week):
    first_day_of_week = datetime.datetime.strptime(f"{year}-W{int(week)}-1", '%Y-W%W-%w').date()
    return first_day_of_week


# print(first_day)

register.filter('count_question', count_question)
register.filter('count_today_tag_question', count_today_tag_question)
register.filter('last_week_tag_question', last_week_tag_question)
