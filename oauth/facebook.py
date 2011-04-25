from urllib import urlopen
from urlparse import parse_qs
import json

class Facebook():
  app_id = '213369482023676'
  api_key = '7abd7099d01cf19aa51550e9c2d5b59f'
  app_secret = '0a45eb54f06087c5b4277ac2e975e1b7'
  contact_email = 'formigarafa@gmail.com'
  redirect_url = 'http://djoylex.xlii.com.br:8000/oauth/facebook/step2'
  def __init__(self):
    self.token = None
    self.code = None
    self.error = None
  def oauth_dialog_url(self):
    return "https://www.facebook.com/dialog/oauth?client_id="+self.app_id+"&redirect_uri="+self.redirect_url
  def token_from_request(self, request):
    if 'error' in request.GET:
      self.error = request.GET['error']
      self.error_reason = request.GET['error_reason']
      self.error_description = request.GET['error_description']
    else:
      self.code = request.GET['code']
      self.token = self.get_token(self.code)
    return self.token
  def profile(self):
    request = urlopen(self.profile_url())
    try:
      response = json.loads(request.read())
    finally:
      request.close()
    return response
  def profile_url(self):
    return "https://graph.facebook.com/me?access_token="+self.token
  def token_url(self, code):
    return "https://graph.facebook.com/oauth/access_token?client_id="+self.app_id+"&redirect_uri="+self.redirect_url+"&client_secret="+self.app_secret+"&code="+code
  def get_token(self, code):
    request = urlopen(self.token_url(code))
    try:
      response = request.read()
    finally:
      request.close()
    data = parse_qs(response)
    return data['access_token'][0]
    