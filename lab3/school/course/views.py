from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def course_select(response, id):
    return HttpResponse("Course ID: %s" % id)
