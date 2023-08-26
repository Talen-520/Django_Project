from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse 
#from .models import Menu

from datetime import datetime

#you can process data for email and form, retreive data from database, transform data, render templates 
#Routing: Map URL to view function
def index(request): 
    return HttpResponse("Hello, world. This is the index view of Demoapp.") 

def menu_by_id(request,menu_id):
    menu = Menu.objects.get(pk=menu_id)
    return HttpResponse(f"{menue.menu_item} : Type of {menue.cuisine} cuisine")

def home(request):
    content = "<html><body><h1>welcome to little lemon </h1></body></html>"
    return HttpResponse(content)

def display_date(request):
    date_joined = datetime.today().year
    return HttpResponse(date_joined)
def menu(request):
    text = """<h1 style = "color:blue">This is little lemon again </h1>"""
    return HttpResponse(text)