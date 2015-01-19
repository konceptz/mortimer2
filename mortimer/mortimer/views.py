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

@login_required(redirect_field_name=None,login_url='/login/')
def home(request):
    """
    output = ""
    for app in AppID.objects.filter(app_user=request.user):
        output += "<div> name: %s, desc: %s </div><br>" %(app.app_name,app.app_desc)
    output += """

    # return HttpResponse(output)

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

    data_dict = {'creds': []}      # if id doesn't belong to user
    output = ""
    if AppID.objects.get(id=request.POST['id']).app_user == request.user:
        '''
        for c in AppData.objects.filter(app_id=request.POST['id']):
            output += "<div> user: %s, pass: %s </div><br>" %(c.username,c.enc_password)
    return HttpResponse(output)
        '''
        data_dict['creds'] = [creds.as_json() for creds in AppData.objects.filter(app_id=request.POST['id'])]

    return HttpResponse(json.dumps(data_dict))#,content_type="application/json")    # another bug :(

@require_POST
@login_required(redirect_field_name=None,login_url='/error/')
def create_app(request):
    """
    Creates a new Application with no credentials
    :params name, description:
    :return success/failure message:
    """

    # needs check to see if it already exists
    if AppID.objects.get(app_user=request.user,app_name=request.POST['name']):
       return HttpResponse("FAIL")

    obj = AppID(app_user=request.user,
          app_name=request.POST['name'],
          app_desc=request.POST['description'])

    try:
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
    app = AppID.objects.get(app_user=request.user,app_name=request.POST['name'])

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