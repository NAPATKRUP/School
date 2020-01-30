from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def manage_student(response):
    return HttpResponse("Manage Page")