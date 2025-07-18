from django.http import HttpResponse

# Create your views here.


def january(request):
    return HttpResponse("this is january")


def february(request):
    return HttpResponse("this is february")