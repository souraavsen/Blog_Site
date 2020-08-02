from django.http import HttpResponse
from django.shortcuts import render

def about(request):
    #return HttpResponse('Hellow World , Which is in About . ')
    return render(request,'about.html')
def homepage(request):
    #return HttpResponse('Its Homepage')
    return render(request, 'homepage.html')
