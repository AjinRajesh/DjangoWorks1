from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views import View

class Studentdetails(View):
    def get(self,request):

        data={'studentname':'Ajin','Age':23,"Course":"Python",'mark':76}

        return JsonResponse(data) #sends data as json

class StudentList(View):
    def get(self,request):

        data=[
            {'studentname': 'Ajin', 'Age': 23, "Course": "Python", 'mark': 96},
            {'studentname': 'Amal', 'Age': 22, "Course": "Python", 'mark': 85},
            {'studentname': 'Alan', 'Age': 21, "Course": "Python", 'mark': 100}
        ]

        return JsonResponse(data,safe=False)#we can only send dictionary directly, for list set safe = False
