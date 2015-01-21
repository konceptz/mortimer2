from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect
from django.utils.decorators import method_decorator
from mortimer.models import AppID, AppData
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.template import RequestContext, loader
import json

def test(request):
    login_template = loader.get_template('test.html')
    context = RequestContext(request,{'apps':AppID.objects.filter(app_user=request.user)})
    return HttpResponse(login_template.render(context))

@login_required(redirect_field_name=None,login_url='/login/')
def home(request):

    login_template = loader.get_template('index.html')
    context = RequestContext(request,{'apps':AppID.objects.filter(app_user=request.user)})
    return HttpResponse(login_template.render(context))

"""
POST requests
create_app - creates a new AppID for the current user (needs app_name & app_desc)
remove_app - deletes an AppID that the current must have access to (needs app_name only)
modify_app - allows user to modify app_name, app_desc or any of the associated creds

send_creds - allows user to send some or all their creds to another user (clone in db)
"""

@require_POST
@login_required(redirect_field_name=None,login_url='/error/')
def get_creds(request):
    id = request.POST.get('id',None)
    if not id:
        return HttpResponse("FAIL")

    data_dict = {'creds': []}      # if id doesn't belong to user
    # check if app_id belongs to user requesting it
    if AppID.objects.get(id=id).app_user == request.user:
        data_dict['creds'] = [creds.as_json() for creds in AppData.objects.filter(app_id=id)]

    return HttpResponse(json.dumps(data_dict))

@require_POST
@login_required(redirect_field_name=None,login_url='/error/')
def create_app(request):
    """
    Creates a new Application with no credentials
    :params name, description:
    :return success/failure message:
    """
    username, description = request.POST.get('name',None), request.POST.get('description',None)

    # validity checks - Todo: replace valid with an error msg to display
    valid = True
    if (not username) or (not description):
        valid = False
    if len(username) > 100 or len(description) > 500:
        valid = False
    if AppID.objects.filter(app_user=request.user,app_name=username).exists(): # needs check to see if it already exists
        valid = False

    if not valid:
       return HttpResponse("FAIL")

    try:
        obj = AppID(app_user=request.user,app_name=username,app_desc=description)
        obj.save()
    except:
        return HttpResponse("FAIL")

    return HttpResponse("OK")

@require_POST
@login_required(redirect_field_name=None,login_url='/error/')
def remove_app(request):
    """
    Removes an existing Application and removes all related credentials
    :param name:
    :return success/failure message:
    """

    app = AppID.objects.get(id=request.POST['id'])  #app_user=request.user,app_name=request.POST['name'])
    if app.app_user != request.user:
        return HttpResponse("FAIL")

    # first clear the appdata table
    try:
        AppData.objects.filter(app_id=app).delete()
        app.delete()
    except:
        return HttpResponse("FAIL")

    return HttpResponse("OK")

def modify_app(request):
    pass

def send_creds(request):
    pass

# ---------------------
# Authentication Views

def log_in(request):
    login_template = loader.get_template('login.html')
    context = RequestContext(request, {})
    return HttpResponse(login_template.render(context))

@require_POST
def authN(request):
    # if not POST request, send blank page
    if not request.POST:
        return HttpResponse()

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    json_response = {}
    json_response['username'] = username

    if user is not None:
        json_response['redirect'] = "/home/"
        json_response['authenticated'] = True
        login(request, user)
        return HttpResponse(json.dumps(json_response), content_type="application/json")
    else:
        json_response['redirect'] = "/"
        json_response['authenticated'] = False
        return HttpResponseForbidden(json.dumps(json_response), content_type="application/json")

def logout_view(request):
    logout(request)
    return redirect("/login")

def error(request):
    return HttpResponse("Something went wrong. A team of highly trained monkeys has been dispatched to deal with the situation")