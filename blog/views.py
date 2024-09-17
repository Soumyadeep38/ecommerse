from django.shortcuts import render
import os

# Create your views here.
def blog(request):
    return render(request, 'blog/blog.html')