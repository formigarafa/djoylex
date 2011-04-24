from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

#import oauth
import oauth.facebook

def step1(request):
  fb = oauth.facebook.Facebook()
  return HttpResponseRedirect(fb.oauth_dialog_url())
  #return HttpResponse(fb.oauth_dialog_url())

  