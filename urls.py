"""GroceryBag URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from myapp.views import register, user_logout, index2, user_login, add, index, update

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register, name='register'),
    path('index2/', index2, name='index2'),
    path('user_login/', user_login, name='user_login'),
    path('logout/', user_logout, name='logout'),
    path('add/', add, name='add'),
    path('index/', index, name='index'),
    path('update/', update, name='update'),

]
