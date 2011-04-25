from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from oauth import Facebook
from blog.models import User

def step1(request):
  return HttpResponseRedirect(Facebook().oauth_dialog_url())

def step2(request):
  facebook_interface = Facebook()
  token = facebook_interface.token_from_request(request)
#  operation_status = "sucesso codigo retornado: (%s).<br/>Token response: (%s)" % (facebook_interface.code, token)
  if token:
    user = User.from_facebook(facebook_interface)
    request.session['user_id'] = user.id
#    profile = facebook_interface.profile()
#    operation_status += "perfil (%s)" % (profile)
#    operation_status += "user (%s)" % (user.username)
    
  return HttpResponseRedirect('/blog/')
  #return HttpResponse(operation_status)
def logout(request):
  del request.session['user_id']
  return HttpResponseRedirect('/blog/')
