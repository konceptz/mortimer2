from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from mortimer.models import AppID
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect

# Leaving this mess for konceptz to clean up :)
@login_required(redirect_field_name=None,login_url='/login/')
def home(response):
    output = ""
    for app in AppID.objects.all():
        output += "<div> name: %s, desc: %s </div><br>" %(app.app_name,app.app_desc)

    return  HttpResponse(output)

# Home with out any no login require - Testing purposes only
def home2(response):
    output = ""
    for app in AppID.objects.all():
        output += "<div> name: %s, desc: %s </div><br>" %(app.app_name,app.app_desc)

    return  HttpResponse(output)

def login(response):
    # Should take creds in a form that posts to authN
    return HttpResponse("Test Login Page")

def authN(request):
    # Stolen from django site
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            return redirect('/')
        else:
            # Return a 'disabled account' error message
            return HttpResponse("Oops, you're account is disabled")
    else:
        # Return an 'invalid login' error message.
        return HttpResponse("Bad username and password")

def logout_view(request):
    logout(request)
    return redirect("/login")