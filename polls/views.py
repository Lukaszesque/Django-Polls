from django.http import HttpResponse

def index(request):
    return HttpResponse("Hi, you're are the polls index.")


