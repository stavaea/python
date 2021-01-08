# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def home(request, id):
    info = 'hello' + id
    return render(request, 'home.html', {'info':info})
    # return HttpResponse('123')