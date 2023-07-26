from django.http import HttpResponse


def index(request):
    return HttpResponse("Welcome!")

def hello(request):
    return HttpResponse("Hello, world.... we meet again.")
