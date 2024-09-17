from django.http import HttpResponse
from django.shortcuts import render


#url routings----with files---#

def home(request):
    return render(request, 'website/index.html')
    # return HttpResponse("this is home page")

def about(request):
    return render(request, 'website/about.html')

def contact(request):
    return render(request, 'website/contact.html')

def blog(request):
    return render(request, 'website/blog.html')

def cart(request):
    return render(request, 'website/cart.html')

def checkout(request):
    return render(request, 'website/checkout.html')

def services(request):
    return render(request, 'website/services.html')

def shop(request):
    return render(request, 'website/shop.html')

def thankyou(request):
    return render(request, 'website/thankyou.html')

def phone(request):
    return HttpResponse("error 404.....")


#url routings----with files---#