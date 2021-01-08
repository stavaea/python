
from django.utils.deprecation import MiddlewareMixin

from django.shortcuts import HttpResponse

class M1(MiddlewareMixin):

    def process_request(self,request):
        print("M1 process_request")
        # if 1:
        #     return HttpResponse("IP禁止")
    def process_response(self, request,response):
        print("M1 process_response")
        return response

class M2(MiddlewareMixin):

    def process_request(self, request):
        print("M2 process_request")

    def process_response(self, request,response):
        print("M2 process_response")
        return HttpResponse("123")