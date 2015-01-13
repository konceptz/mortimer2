from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from mortimer.models import AppID
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.template import RequestContext, loader

@login_required(redirect_field_name=None,login_url='/login/')
def home(request):
    output = ""
    for app in AppID.objects.all():
        output += "<div> name: %s, desc: %s </div><br>" %(app.app_name,app.app_desc)

    return HttpResponse(output)


# Home with out any no login require - Testing purposes only
'''
def home2(response):
    output = ""
    for app in AppID.objects.all():
        output += "<div> name: %s, desc: %s </div><br>" %(app.app_name,app.app_desc)

    return  HttpResponse(output)
'''

def log_in(request):
    login_template = loader.get_template('login.html')
    context = RequestContext(request, {})
    return HttpResponse(login_template.render(context))


def authN(request):
    # Stolen from django site
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/home/')
    else:
        # Return an 'invalid login' error message.
        #return HttpResponse("Bad username and password")
        return redirect('/')

def logout_view(request):
    logout(request)
    return redirect("/login")
