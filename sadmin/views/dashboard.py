from django.http.response import HttpResponse
from django.shortcuts import render, redirect, get_list_or_404
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib import messages


class Dashboard(View):
    def get(self,request,*args,**kwarsgs):
        return HttpResponse("<h1> Hello guys</h1>")