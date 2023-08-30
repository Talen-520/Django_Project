from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse , HttpResponseNotFound
#from .models import Menu

from datetime import datetime

#you can process data for email and form, retreive data from database, transform data, render templates 
#Routing: Map URL to view function
def index(request): 
    return HttpResponse("Hello, world. This is the index view of Demoapp.") 

def menu_by_id(request,menu_id):
    menu = Menu.objects.get(pk=menu_id)
    return HttpResponse(f"{menue.menu_item} : Type of {menue.cuisine} cuisine")
'''
def home(request):
    content = "<html><body><h1>welcome to little lemon </h1></body></html>"
    return HttpResponse(content)
'''
#method display request attributes

def attributes(request):
    path = request.path
    schema = request.scheme
    method = request.method
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info

    response = HttpResponse()
    response.headers['Age'] = 20

    msg = f"""<br>
    <br>Path: {path}
    <br>Schema: {schema}
    <br>Method: {method}
    <br>Address: {address}
    <br>User Agent: {user_agent}
    <br>Path Info: {path_info}
    <br>Response header: {response.headers}
    """
    return HttpResponse(msg, content_type="text/html",charset="utf-8")

def display_date(request):
    date_joined = datetime.today().year
    return HttpResponse(date_joined)
def menu(request):
    text = """<h1 style = "color:blue">This is little lemon again </h1>"""
    return HttpResponse(text)
#render webpage 
from django.template import loader 
def loader(request): 
    template = loader.get_template('demoapp/index.html') 
    context={}  
    return HttpResponse(template.render(context, request)) 


def ServerStatus(request): 
    path = request.path 
    method = request.method 
    content=''' 
<center><h2>Testing Django Request Response Objects</h2> 
<p>Request path : " {}</p> 
<p>Request Method :{}</p></center> 
'''.format(path, method) 
    return HttpResponse(content) 


def menuitems(request,dish):
    items = {
        'pasta':'pasta with red sauce',
        'falafel':'falafel with hummus',
        'cheesecake':'cheesecake with cherry topping',
    }
    description = items [dish]   
    return HttpResponse(f"<h2>{dish}</h2>" + description)



def qryview(request): 
    name = request.GET['name'] 
    id = request.GET['id'] 
    return HttpResponse("Name:{} UserID:{}".format(name, id)) 

#error handling example , need turn off debug mode
def error_handling(request): 
    # ... 
    if condition==True: 
        return HttpResponse('<h1>Page not found</h1>', status_code='404') 
    else: 
        return HttpResponse('<h1>Page was found</h1>') 
# permission denied
def myview(request): 
    if not request.user.has_perm('myapp.view_mymodel'): 
        raise PermissionDenied() 
    return HttpResponse() 

from demoapp.forms import LogForm

def form_view(request):
    form = LogForm()
    if request.method == 'POST':
        form = LogForm(request.POST)# update the form object with the contents of post inside the request object
        if form.is_valid():
            form.save()
            return HttpResponse("form saved")
    context = {'form':form}
    #return render(request, 'demoapp/form.html', context)
    return render(request, 'home.html', context)