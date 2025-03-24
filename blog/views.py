from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


# Create your views here.
def home(request):
    return HttpResponse("Hello Django!")


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Бұл бет табылмады!</h1>")