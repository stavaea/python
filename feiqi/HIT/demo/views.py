# coding:utf_8
from django.shortcuts import render

# Create your views here.

# def f(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     else:
#         return f(n-1)+f(n-2)


def index(request):
    # return render(request, 'home.html', {'message': True})
    # return render(request, 'home.html', {'message': [0, 1, 2, 3]})

    # data = {'flag': True, 'students':
    #     [
    #         {'id': 1801, 'name': '张三', 'salary': 6000},
    #         {'id': 1802, 'name': '田老师', 'salary': 7500},
    #         {'id': 1803, 'name': '李四', 'salary': 10000}
    #     ]
    #         }
    # return render(request, 'home.html', data)
    return render(request, 'home.html', )

def case(request):
    data = {'cases':
        [
            {'id': 2, 'title': '登录接口正向流程'},
            {'id': 25, 'title': '登录接口-用户名为空'},
            {'id': 30, 'title': '登录接口-密码错误'}
        ]
}

    return render(request, 'cases.html', {'message': data})

def task(request):
    # return render(request, 'home.html', {'message': True})
    # return render(request, 'home.html', {'message': [0, 1, 2, 3]})

    data = {'flag': True, 'tasks':
        [
            {'id': 1801, 'name': '接口任务一', 'link': 'task1'},
            {'id': 1802, 'name': '回归测试任务二', 'link': 'task222'},
            {'id': 1803, 'name': '线上测试04-21', 'link': 'task0421'},
        ]
            }
    return render(request, 'task_new.html', data)