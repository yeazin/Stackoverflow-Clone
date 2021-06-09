from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from django.utils.decorators import method_decorator
from django.contrib import messages

from question.models import Question
# import from basis
from .forms import QuestionForms


# Questions view 
class AllQuestions(View):
    def get(self,request,*args,**kwargs):
        context={

        }
        return render (request,'question/q/questions.html', context)

# View single Question 
class SingleQuestion(View):
    def get(self,request,id):
        question_obj = get_object_or_404(Question,id=id)
        question_obj.views_count = question_obj.views_count + 1
        question_obj.save()
        context={
            'question':question_obj
        }
        return render(request,'question/q/single_question.html', context)

# Tags View 
class AllTags(View):
    def get(self,request,*args,**kwargs):
        context ={

        }
        return render (request,'question/tags/tags.html',context)


