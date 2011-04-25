from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from oauth import Facebook

def step1(request):
  return HttpResponseRedirect(Facebook().oauth_dialog_url())

def step2(request):
  if 'error' in request.GET:
    error = request.GET['error']
    error_reason = request.GET['error_reason']
    error_description = request.GET['error_description']
    operation_status = 'Falha (%s): %s - %s' % (error, error_reason, error_description)
  else:
    code = request.GET['code']
    fb = Facebook()
    token = fb.get_token(code)
    operation_status = "sucesso codigo retornado: (%s). Token response: (%s)" % (code, token)
  return HttpResponse(operation_status)