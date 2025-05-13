from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.cache import cache_page
from django.core.cache import cache
import time
from .tasks import sendEmail
import requests

def send_email(request):
    sendEmail.delay()
    return HttpResponse("<h1>Done Sending</h1>")

## from django.core.cache import cache ##
# def test(request):
#     if cache.get("test_delay_api") is None:
#         response = requests.get("https://bd5a0fc4-e2b9-4dda-be77-c569b41ac786.mock.pstmn.io/test/delay/5")
#         cache.set("test_delay_api",response.json(),60)
#     return JsonResponse(cache.get("test_delay_api"))


# [Decorator Cache] # from django.views.decorators.cache import cache_page ## 
@cache_page(60) # time
def test(request): 
    response = requests.get("https://bd5a0fc4-e2b9-4dda-be77-c569b41ac786.mock.pstmn.io/test/delay/5")
    return JsonResponse(response.json())



