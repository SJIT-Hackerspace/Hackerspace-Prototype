from django.shortcuts import render
from django.http import HttpResponse
import requests
import os
import json
#import ast

# Create your views here.
def home(request):
	return render(request,"home.html",{})
def a(request):
	return render(request,"bfs.txt",{})
def login(request):
	return render(request,"login.html",{})
def feed(request):
	return render(request,"feed.html",{})
def get(request):
	requestdict = request.POST
	source = requestdict["source"]
	lang = "5"
	testcases = ""
	url = "api.hackerrank.com/checker/submission.json"
	api_key = "hackerrank|161256-622|faa76a548e2dce2ef37df6a68d4dc0c75bd760f3"
	r = requests.post("http://api.hackerrank.com/checker/submission.json", data = {
	    "source" : source,
	    "lang" : lang,
	    "testcases" : json.dumps([testcases]),
	    "api_key" : api_key
	})
	result = r.json()
	return HttpResponse(result['result']['stdout'][0]+ "<br>" +str(result['result']['time'][0]))


"""def auth_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username = username, password = password)

    if user is not None:
        auth.login(request, user)
        return HttpResponseRedirect('/home.html')
    else:
        return HttpResponseRedirect('/')"""
