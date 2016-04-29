from django.shortcuts import render
from django.http import HttpResponse
from data.models import notify
import json
# Create your views here.

def home(request):
	return HttpResponse('Welcome to Notification')

def notify_list(request):
    all_notification = notify.objects.all()
    my_response = []
    for i in all_notification:
        single_notify_dict = {}
        single_notify_dict['string1'] = i.string1
        single_notify_dict['string2'] = i.string2
        single_notify_dict['string3'] = i.string3
        single_notify_dict['string4'] = i.string4
        my_response.append(single_notify_dict)

    my_response = json.dumps(my_response)
    return HttpResponse(my_response)
