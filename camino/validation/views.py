from django.http import HttpResponse, HttpResponseRedirect, Http404
#from .models import Question, Choice
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

def index(request):
    return HttpResponse("Hello and welcome to Ashay Vipinkumar's Classroom Validation Service!")
