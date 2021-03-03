from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from myapp.forms import UserForm
from myapp.models import UserProfileInfo, GroceryList
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.

def index2(request):
    return render(request, 'index2.html', {})


@login_required
def special(request):
    return HttpResponse("You are logged in !")


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index2'))


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request, 'registration.html',
                  {'user_form': user_form,
                   'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('index2'))
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(
                username, password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'login.html', {})


def add(request):
    List = GroceryList()
    if request.method == 'POST':
        List.ItemName = request.POST.get('ItemName', '')
        List.ItemQuantity = request.POST.get('ItemQuantity', '')
        List.ItemStatus = request.POST.get('ItemStatus', '')
        List.Date = request.POST.get('Date', '')
        List.save()
        add = True
        return render(request, 'index.html', {'GroceryList': List})
    return render(request, 'add.html', {})


def home(request):
    List = GroceryList.objects.all()
    return render(request, 'index.html', {'GroceryList': List})


def update(request):
    List = GroceryList.objects.all()
    if request.method == 'POST':
        id = request.POST['ItemName']
        updateList = GroceryList.objects.get(id=id)
        updateList.ItemQuantity = request.POST.get('ItemQuantity', '')
        updateList.ItemStatus = request.POST.get('ItemStatus', '')
        updateList.Date = request.POST.get('Date', '')
        updateList.save()
        return render(request, 'index.html', {'GroceryList': List})

    return render(request, 'update.html', {'GroceryList': List})
