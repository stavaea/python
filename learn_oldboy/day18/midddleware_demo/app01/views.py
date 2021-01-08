from django.shortcuts import render,HttpResponse


# Create your views here.



def index(request):


    print("index....")

    return HttpResponse("index")