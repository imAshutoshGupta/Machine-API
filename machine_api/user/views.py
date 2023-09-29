from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt #used to bypass csrf token
from .models import Client, Project,User
import json
import datetime

# Create your views here.
@csrf_exempt
def get_client(request):
    c=Client.objects.all()
    print(c)
    context={}
    #context['clients']=c
    i=0
    for x in c:
        context[i]={
            'id':x.id,
            'client_name':x.client_name,
            'created_by':x.uid.first_name
        }
        i+=1
        
    # res = {'success':'response from get client'}
    json_data = json.dumps(context)
    return HttpResponse(json_data)

@csrf_exempt                        #decorator used to bypass csrf token
def create_client(request):


    print(request.method)
    print(request.POST)
    print(type(request.POST))
    
    
    cname = request.POST['cname']
    user_id =  request.POST['user_id']
    u = User.objects.filter(id=user_id)  #select * from auth_user where id=user_id;
    print(u)
    print(u[0])
    c = Client.objects.create(client_name=cname,uid=u[0])
    c.save()

    res = {'success':'response from post client'}
    json_data = json.dumps(res)
    return HttpResponse(json_data)

@csrf_exempt 
def update_client(request,rid):

    print(request.method)
    print(request.POST)
    print(request.body)

    d=json.loads(request.body)
    
    print(d)
    print(type(d))
    print("record id:", rid)

    ucname=d['cname']
    c=Client.objects.filter(id=rid)
    print(c)
    c.update(client_name=ucname, updated_at=datetime.datetime.now())
    res = {'success':'client updated successfully'}
    json_data = json.dumps(res)
    return HttpResponse(json_data)

@csrf_exempt 
def delete_client(request,rid):
    c=Client.objects.filter(id=rid)
    c.delete()

    res = {'success':'deleted successfully'}
    json_data = json.dumps(res)
    return HttpResponse(json_data)