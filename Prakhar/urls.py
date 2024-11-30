"""
URL configuration for Prakhar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from Portfolio import views as v
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home' , v.home_page , name="Site_home"),
    path('login' , v.user_login , name="login_user"), 
    path('logout' , v.user_logout , name="logout_user"), 
    path('portfolio' , v.portfolio , name="portfolio"), 
    path('save' , v.Save_contact , name = "Save_contact"),
    path('PythonProjects' , v.show_pp , name = "projects"),
    path('resume' , v.resume , name = "resume"),
    path('' , v.register , name = "register"),
]
