from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from oauth import Facebook

def step1(request):
  return HttpResponseRedirect(Facebook().oauth_dialog_url())

def step2(request):
  facebook_interface = Facebook()
  token = facebook_interface.token_from_request(request)
  operation_status = "sucesso codigo retornado: (%s).<br/>Token response: (%s)" % (facebook_interface.code, token)
  return HttpResponse(operation_status)