from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django.contrib import messages
from question.models import Tags
from question.models import Question
# import from basis
from .forms import QuestionForms
from .models import Answer, Question
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Questions view 
class AllQuestions(View):
    def get(self, request, *args, **kwargs):
        question_obj = Question.objects.all().order_by('-created_at')
        context = {
            'question': question_obj,
        }
        return render(request, 'question/questions.html', context)


# View single Question
class SingleQuestion(View):
    def get(self, request, id):
        question_obj = get_object_or_404(Question, id=id)
        question_obj.views_count = question_obj.views_count + 1
        question_obj.save()
        context = {
            'question': question_obj
        }
        return render(request, 'question/single_question.html', context)


# Tags View
class AllTags(View):
    def get(self, request, *args, **kwargs):
        all_tags = Tags.objects.all().order_by('tag')
        page = request.GET.get('page', 1)
        # call django built in pagination class
        paginator = Paginator(all_tags, per_page=2)
        try:
            tags = paginator.page(page)
        except PageNotAnInteger as e:
            tags = paginator.page(1)
        except EmptyPage:
            tags = Paginator.page(paginator.num_pages)
        context = {
            'tags': tags
        }
        return render(request, 'tags/tags.html', context)

# single Tag view
class SingleTagView(View):
    def get(self,request,id,*args,**kwargs):
        tag_obj = get_object_or_404(Tags,id=id)
        tag_obj_question = Question.objects.filter(tags=tag_obj)
        question_count = tag_obj_question.count()
        context ={
            'tag_name':tag_obj,
            'question':tag_obj_question,
            't_count':question_count
        }
        return render(request,'tags/single_tag.html',context)

def search_tag(request):
    if request.method == "GET":
        search_text = request.GET['search_text']
        # print(search_text)
        if search_text is not None and search_text != u"":
            search_text = request.GET['search_text']
            tags = Tags.objects.filter(tag__contains=search_text)
        else:
            tags = []

        return render(request, 'tags/tag_search_ajax.html', {'tags': tags})


# for testing purpose
def upvote_template(request):
    answers = Answer.objects.all()
    return render(request, 'upvote.html', {'answers': answers})


def upvote(request):
    if request.method == "POST":
        answer_id = request.POST.get('answerId')
        action_type = str(request.POST.get('action'))
        print(answer_id, action_type)
        if action_type.lower() == 'up':
            answer = Answer.objects.get(id=answer_id)
            answer.vote += 1
            answer.save()
        elif action_type.lower() == 'down':
            answer = Answer.objects.get(id=answer_id)
            answer.vote -= 1
            answer.save()
        return JsonResponse({'status': "ok", "vote": answer.vote, 'id': answer.id})
