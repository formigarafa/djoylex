from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response

from oauth import Facebook
from blog.models import User

def step1(request):
  return HttpResponseRedirect(Facebook().oauth_dialog_url()+"&display=popup")

def step2(request):
  facebook_interface = Facebook()
  token = facebook_interface.token_from_request(request)

  if token:
    user = User.from_facebook(facebook_interface)
    request.session['user_id'] = user.id

  return render_to_response('step2.html')

def logout(request):
  del request.session['user_id']
  return HttpResponseRedirect('/blog/')
