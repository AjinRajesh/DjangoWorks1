from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
#
#function based
# def firstpage(request):
#     if request.method=='GET':
#         return HttpResponse("First Page")
#
# def secondpage(request):
#     if request.method=='GET':
#         return HttpResponse("Second Page")

#class based
from django.views import View

class Firstpage(View):
    def get(self,request):
        return HttpResponse("First Page")

class Secondpage(View):
    def get(self,request):
        return HttpResponse("Second Page")
