from django.core.handlers.wsgi import get_bytes_from_wsgi
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, requires_csrf_token
import json
from django.core.handlers import wsgi


@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        return HttpResponse("Webhook received! POST", request)

    if request.method == 'GET':
        print("Data received from Webhook is GET: ", request)
        return HttpResponse("Webhook received! GET", request)

