from django.shortcuts import render
from django.http import HttpResponse 
from django.shortcuts import render
# Create your views here.

def print_hello(request):
    movie_data={
        'movies' :  [
        {
        'title':'Godfather',
        'year':1990,
        'summary':'story of an underworld king',
        'success':False
    },
    {
        'title':'Titanic',
        'year':2002,
        'summary':'story of an underworld king',
        'success':True
    },
    {
        'title':'Goldfish',
        'year':1990,
        'summary':'story of an underworld king',
        'success':False
    }
    
    ]}
    return render(request,'hello.html',movie_data)

