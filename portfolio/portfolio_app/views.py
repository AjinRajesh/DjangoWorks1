from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

# Create your views here.
class About(View):
    def get(self,request):
        data={'id':1,
              'Full Name':'Ajin Rajesh',
              'Title':'Python Developer',
              'DOB':'24-12-2002',
              'email':'ajinrajesh234@gmail.com',
              'contact':'9876543210',
              'location':'Kannur',
              'github_url':'https://github.com/AjinRajesh',
              'linkedin_url':'https://www.linkedin.com/in/ajinrajesh'
              }
        return JsonResponse(data)

class Education(View):
    def get(self,request):
        data={
            'institution':'Model Engineering College',
            'course':'B.Tech Computer Science and Engineering',
            'university':'APJ Abdul Kalam Technological University',
            'location':'Kochi',
            'start_year':2022,
            'end_year':2026,
            'grade':'7.0 CGPA',
            'description':'Computer Science Engineering'
        }
        return JsonResponse(data)

class Projects(View):
    def get(self,request):
        data=[
            {
                'id':1,
                'projectname':'MLSQL',
                'description':'Malayalam natural language query to sql query generation system',
                'technologies':'Python,Sarvam AI,SQL,LoRA',
                'duration':'6 months',
                'live_url':'https://example.com/mlsql'
            },
            {
                'id': 2,
                'projectname': 'Blood Bank Management System',
                'description': 'App to manage blood donors and check blood availability',
                'technologies': 'Python,Streamlit,MySQL',
                'duration': '1 day',
                'live_url': 'https://example.com/blood-bank'
            }
        ]
        return JsonResponse(data,safe=False)
