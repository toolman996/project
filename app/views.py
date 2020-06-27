from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('提交')


def indexx(request):
    print()
    return HttpResponse('提交')