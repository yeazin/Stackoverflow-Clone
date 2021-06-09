from django.shortcuts import render
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponseRedirect
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login,logout
from django.utils.decorators import method_decorator
from django.contrib import messages
# import from basis
from .forms import QuestionForms

# Create Questions
class CreateQuestion(View):
    def get(self,request,*args,**kwrargs):
        q_forms = QuestionForms
        context={
            'forms':q_forms
        }
        return render(request,'question/create_q.html',context)

# Questions view 
class AllQuestions(View):
    def get(self,request,*args,**kwargs):
        context={

        }
        return render (request,'question/q/questions.html', context)

# Tags View 
class AllTags(View):
    def get(self,request,*args,**kwargs):
        context ={

        }
        return render (request,'question/tags/tags.html',context)


