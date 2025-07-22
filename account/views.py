from codecs import register
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import RegistrationForm, LoginForm
from django.contrib.auth.models import auth
from .models import Account

# Create your views here.
def acc_home(request):
    accounts = Account.objects.all()
    context={'accounts': accounts}
    return render(request, 'account/acc_home.html', context)


def register(request):
    form = RegistrationForm()

    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")
        
    context ={'registerform':form}
    return render(request, 'account/register.html', context)    



def login(request):
    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            Account = authenticate(request, username=username, password=password)

            if Account is not None:

                auth.login(request, Account)

                return redirect("account:dashboard")
            
    context = {'loginform':form}
    return render(request, 'account/login.html', context)


def logout(request):

    auth.logout(request)

    return redirect("giox:giox_home")            


def dashboard(request):
    return render(request, 'account/dashboard.html', {})

def must_authenticate_view(request):
    return render(request, 'account/must_authenticate.html', {})



"""def registration_view(request):
    context ={}
    if request == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email= form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password1=raw_password) 
            login(request, account)
            return redirect('giox_home')
        else:
            context['registration_form'] = form
    else:
        form = RegistrationForm()
        context['registration_form']= form
    return render(request, 'account/register.html', context) """
   



