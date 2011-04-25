from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from oauth import Facebook

def step1(request):
  fb = Facebook()
  return HttpResponseRedirect(fb.oauth_dialog_url())

def step2(request):
  code = request.GET['code']
  return HttpResponse(code)
  