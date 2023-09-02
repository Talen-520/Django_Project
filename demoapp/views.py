from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse , HttpResponseNotFound
#from .models import Menu

from datetime import datetime

#you can process data for email and form, retreive data from database, transform data, render templates 
#Routing: Map URL to view function
def index(request): 
    return HttpResponse("Hello, world. This is the index view of Demoapp.") 

def menu(request):
    #menuitem = {"name" : "Greek salad"} #single item use {{name}}
    #mutilple items
    #use {% for item in mains %}
    #{{}}
    #{% endfor %}
    menuitem = {'mains':[
        {"name":"Greek salad","price":"12"},
        {"name": 'shawarama',"price":"15"},
        {"name": 'pizza',"price":"20"},
        {"name": 'pasta',"price":"25"},
        ]}
    return render(request,'menu.html',menuitem)
from .models import Menu    
#load database to display content
def menu_by_id(request):
    newmenu = Menu.objects.all()
    newmenu_dict = {"menu":newmenu}
    return render(request,"menu_cards.html",newmenu_dict)
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

from demoapp.forms import surveyForm
def form_survey(request):
    form = surveyForm()
    if request.method == 'POST':
        form = surveyForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("form submitted")
    context = {'form':form}
    #return render(request, 'demoapp/form.html', context)
    return render(request, 'survey.html', context)

#dynamic content
def about(request):
    abount_content = {'about': "Base in Chicago, Illinonios, Little Lemon is a blalalalala "} #about is key mapped in the html page see {{about}}
    return render(request,"about.html",abount_content)

#loging 
'''
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

#load database to display content
from .models import Menu    
def menu_by_id(request):
    newmenu = Menu.objects.all()
    newmenu_dict = {"menu":newmenu}
    return render(request,"menu_cards.html",newmenu_dict)
'''

#signup user
from .models import userinformation
from django.contrib.auth import login
from django.contrib.auth import authenticate


from demoapp.forms import userform
def signup(request):
    form = userform()
    if request.method == 'POST':
        form = userform(request.POST)# update the form object with the contents of post inside the request object
        if form.is_valid():
            form.save()
            return HttpResponse("signup successed")
    context = {'form':form}
    #return render(request, 'demoapp/form.html', context)
    return render(request, 'signup.html', context)

#login user
from demoapp.forms import userform
from django.contrib import messages
from django.shortcuts import render, redirect


def login(request):
    if request.method == 'POST':
        form = userform(request.POST)
        if form.is_valid():
            # Get the user input from the form
            user_input = form.cleaned_data['username']
            pass_input = form.cleaned_data['password']
            # Check if the user input exists in the database
            if userinformation.objects.filter(username=user_input).exists() and userinformation.objects.filter(password=pass_input).exists() :
                # Match found in the database
                return HttpResponse("Login successed")
            else:
                # No match found in the database
                #return HttpResponse("invaild password or username")
                error_message = "Invalid password or username"
                # Redirect back to the login form
                return render(request, 'login.html', {'form': form, 'error_message': error_message})
    else:
        form = userform()
    return render(request, 'login.html', {'form': form})  # Replace 'login.html' with your login template name