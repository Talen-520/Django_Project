"""
URL configuration for demoproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path

from demoapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    #execute on the homepage so I can just replace the word admin with an empty string
    #
    path('', views.index, name = 'index'),#http://127.0.0.1:8000/ view.index function be called
    #path('demo/', include('demoapp.urls')), use this way by create urls.py in demoapp and add path('demo/', include('demoapp.urls')) in demoproject\urls.py
]
#http://127.0.0.1:8000/admin/ admin page