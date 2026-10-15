from django.shortcuts import render
from django.views import View
from movies.models import Movie
from django.http import JsonResponse

# Create your views here.
class Movielist(View):
    def get(self,request):
        data=list(Movie.objects.all().values())
        return JsonResponse(data,safe=False)

