from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt #used to bypass csrf token
import json

# Create your views here.
def get_client(request):
    res = {'success':'response from get client'}
    json_data = json.dumps(res)
    return HttpResponse(json_data)

@csrf_exempt                        #decorator used to bypass csrf token
def create_client(request):
    res = {'success':'response from post client'}
    json_data = json.dumps(res)
    return HttpResponse(json_data)

@csrf_exempt 
def update_client(request):
    res = {'success':'client updated successfully'}
    json_data = json.dumps(res)
    return HttpResponse(json_data)

@csrf_exempt 
def delete_client(request):
    res = {'success':'deleted successfully'}
    json_data = json.dumps(res)
    return HttpResponse(json_data)