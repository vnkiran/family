"""bikes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.conf import  settings
from .views import bike,contact,hero,bajaj,honda,login_user,register,logout_user,kiran,nalini
urlpatterns = [
    path('admin/', admin.site.urls),
    path("home/",bike,name="home"),
    path("contact/",contact,name="contact"),
    path("hero/",hero,name="hero"),
    path("bajaj/",bajaj,name="bajaj"),
    path("honda/",honda,name="honda"),
    path("kiran/",kiran,name="kiran"),
    path("nalini/",nalini,name="nalini"),
    path("",login_user,name="login"),

    path("register/",register,name="register"),
    
    path("logout/",logout_user,name="logout"),
    
   

]
urlpatterns  += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
