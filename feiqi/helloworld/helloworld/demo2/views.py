from django.shortcuts import render

# Create your views here.

def home(request, id):
    #return HttpResponse('hello world')
    info = 'huice'+id
    return render(request, 'home.html', {'info':info})

