from django.urls import path , re_path
from . import views  #in same directory use .
from . import forms
urlpatterns = [ 
    path('', views.index, name='index'), 
    #The first argument is the route, which is a string that contains a URL pattern,
    #  and the second argument is the view, which contains the relative path and the name of the view function.
    path('attributes/',views.attributes), #(http://127.0.0.1:8000/home, home function in views.py)
    path('display_date/',views.display_date), 
    path('menu/',views.menu),
    #path('loader/',views.loader),
    path('ServerStatus/',views.ServerStatus),
    path('dishes/<str:dish>',views.menuitems),#http://127.0.0.1:8000/dishes/pasta
    path('getuser/', views.qryview, name='qryview'),#http://127.0.0.1:8000/getuser/?name=John&id=1
    #path('login/', views.login, name='login') ,

    # forms.py
    path('home/', views.form_view) ,

] 