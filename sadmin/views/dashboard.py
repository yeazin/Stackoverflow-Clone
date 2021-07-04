from django.shortcuts import render, redirect, get_list_or_404
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib import messages