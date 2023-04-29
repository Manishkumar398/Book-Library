from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Book



def home(request):
    books=Book.objects.all()
    return render(request,'library/home.html',{"books":books})