import datetime as dt
import json
from secrets import compare_digest

from django.conf import settings
import requests
from django.db.transaction import atomic, non_atomic_requests
from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils import timezone
from requests import Response

from rest_framework.views import APIView

from client.serializer import ClientSerializer


class WebhookAPIView(APIView):

    def post(self, request):
        number = request.GET.get('PhoneClient')
        comment = request.GET.get('Comment')

        response = requests.post(
            f'https://okna360-crm.ru/ERPOKNA360/AddNewCalls.php?'
            f'key=d41d8cd98f00b204e9800998ecf8427e&PhoneClient={number}&Comment=САЙТ {comment}')

        return HttpResponse("Webhook received! POST", request)
# @csrf_exempt
# @require_POST
# def webhook(request):
#     if request.method == 'POST':
#         print(request.GET)
#         data = json.loads(request.body.decode("utf-8"))
#         print(data)
#     return HttpResponse(f"Message received okay.{request.POST} {request.body}", content_type="text/plain")
