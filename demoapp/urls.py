from django.urls import path 
from . import views  #in same directory use .

urlpatterns = [ 
    path('', views.index, name='index'), 
    #The first argument is the route, which is a string that contains a URL pattern,
    #  and the second argument is the view, which contains the relative path and the name of the view function.
    path('home/',views.home), #(http://127.0.0.1:8000/home, home function in views.py)
    path('display_date/',views.display_date), 
    path('menu/',views.menu),
] 