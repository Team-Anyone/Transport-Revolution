from django.shortcuts import render
from django.http import HttpResponse

# or from firstapp import forms
# Create your views here.
def homepage(request):
    return render(request,'first_app/homepage.html')

def description(request):
    return render(request,'first_app/description.html')

def case_study(request):
    return render(request,'first_app/case_study.html')
