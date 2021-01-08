from django.shortcuts import render
import time
import os
import subprocess
# Create your views here.

def new(request):
    return render(request, 'case.html')


def run(request):
    data = request.POST.get('data')
    p_name = request.POST.get('name')
    if data and p_name:
        name = time.strftime('%Y_%m_%d_%H-%M-%S', time.localtime(time.time()))
        steps = data.split('&')
        with open('./cases/%s.txt' % name, 'wb') as f:
            f.write(('*** Settings ***' + '\n').encode("utf8"))
            f.write(('Library    Selenium2Library' + '\n').encode("utf8"))
            f.write(('*** Test Cases ***' + '\n').encode("utf8"))
            f.write((p_name + '\n').encode("utf8"))
            for step in steps:
                line = ''
                type = step.split('=')[0]
                values = step.split('=')[1]
                if type == '1001':
                    line = '    Open Browser    ' + values
                elif type == '1002':
                    line = '    Input Text    ' + values
                elif type == '1003':
                    line = '    Click Element    ' + values
                f.write((line + '\n').encode("utf8"))
            print('robot ./cases/%s.txt' % name)
            os.system('robot ./cases/%s.txt' % name)
            return render(request, 'case.html')
    else:
        return render(request, 'case.html')