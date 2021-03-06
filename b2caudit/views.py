from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

def getToken(request):
    url = 'https://login.microsoftonline.com/ssopb2cseneca.onmicrosoft.com/oauth2/token?api-version=1.0'
    body = {
        'grant_type': 'client_credentials',
        'resource': 'https://graph.microsoft.com',
        'client_id': 'c69f8e8c-0506-4736-8d5e-6db120e3182e',
        'client_secret': 'NCXpUub3oYEmdsGIi[6QJPY8t5[UCu?_'
    }
    resp = requests.post(url, body)
    #this line converts the response to a python dict which can then be parsed easily
    #response_native = json.loads(resp.text)
    #oauthToken = response_native.get('access_token')
    token_type = json.loads(resp.text).get('token_type')
    access_token = json.loads(resp.text).get('access_token')
    #return HttpResponse(token_type + ' ' + access_token)
    token = {token_type: json.loads(resp.text).get('token_type'), access_token: json.loads(resp.text).get('access_token')  }
    return render(request, 'showToken.html', {'access_token': access_token})

def getAuditLog(self):
    return HttpResponse('GetAuditLog Here')
