from django.db.models import Model
from django.shortcuts import render


# Create your views here.
from django.http import JsonResponse
from django.views import View

# class Studentdetails(View):
#     def get(self,request):
#
#         data={'studentname':'Ajin','Age':23,"Course":"Python",'mark':76}
#
#         return JsonResponse(data) #sends data as json

from app.models import Student
class StudentList(View):
    def get(self,request):

        # data=[
        #     {'studentname': 'Ajin', 'Age': 23, "Course": "Python", 'mark': 96},
        #     {'studentname': 'Amal', 'Age': 22, "Course": "Python", 'mark': 85},
        #     {'studentname': 'Alan', 'Age': 21, "Course": "Python", 'mark': 100}
        # ]

        #to retrive data from database table
        #modelname.objects.all()
        qs=Student.objects.all()
        # print()
        # print(type(data))
        # print()
        data=list(Student.objects.all().values())#list of dictionaries, include .values()
        print(data)

        return JsonResponse(data,safe=False)#we can only send dictionary directly, for list set safe = False

#API view for inserting new value
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from json import loads
@method_decorator(csrf_exempt,name='dispatch')
class Studentcreate(View):
    def post(self,request):
        #fetch the data from client side
        form_data=request.body #json format

        #converts the json data into python type
        data=loads(form_data) #python native(dictionary)

        #stores the data into db table using orm query
        print(data)
        s=Student.objects.create(name=data['name'],age=data['age'],course=data['course'],marks=data['marks'])
        s.save()

        #return response back to client
        return JsonResponse('Message created',safe=False)

#API view for retrieveing single record
class StudentDetail(View):
    def get(self,request,i):#i stores the id value from client
        # read records matching with id from db table
        qs=Student.objects.filter(id=i)
        #convert the data into python native
        data=list(qs.values())
        #sends the response
        return JsonResponse(data,safe=False)

# API view for deleting a specific record
@method_decorator(csrf_exempt,name='dispatch')
class StudentDelete(View):
    def delete(self,request,i):
        #read the record matching with id from db table
        s=Student.objects.get(id=i)

        #delete the record
        s.delete()
        #sends the response
        return JsonResponse({'message':'Deleted Successfully'})

#API view for updating(fully) existing record
@method_decorator(csrf_exempt,name='dispatch')
class StudentUpdate(View):
    def put(self,request,i):
        #fetching json data
        form_data=request.body
        #converting data to python native(dictionary)
        data=loads(form_data)
        #fetching student object based on id
        s=Student.objects.get(id=i)
        #updating each value
        s.name=data['name']
        s.age=data['age']
        s.course=data['course']
        s.marks=data['marks']
        #saves the record
        s.save()
        #return Response
        return JsonResponse({'message':'Updated Successfully'})


#API view for updating partially
@method_decorator(csrf_exempt,name='dispatch')
class StudentpartialUpdate(View):
    def patch(self,request,i):
        s=Student.objects.get(id=i)
        form_data=request.body

        data=loads(form_data)

        if 'name' in data:
            s.name=data['name']
        if 'age' in data:
            s.age=data['age']
        if 'course' in data:
            s.course=data['course']
        if 'marks' in data:
            s.marks=data['marks']
        s.save()

        return JsonResponse({'message':'Updated Partially'})