from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def first (request):
     return HttpResponse('HAI IAM NEW HERE')

def second (request):
     return HttpResponse('Save Money')