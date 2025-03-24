from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
menu = ["About", "Contact", "Blog"]


def home(request):
    data = {"title": "NurbekTech", "menu": menu}
    return render(request, "blog/index.html", context=data)


def about(request):
    return render(request, "blog/about.html", {"title": "ABOUT"})


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Бұл бет табылмады!</h1>")
