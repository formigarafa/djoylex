from django.db import models

# Create your models here.
class User(models.Model):
  facebook_access_token = models.CharField(max_length=255)
  facebook_id = models.CharField(max_length=30)
  username = models.CharField(max_length=20)
  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)
  @staticmethod
  def from_facebook(facebook):
    profile = facebook.profile()
    user = User()
    user.facebook_access_token = facebook.token
    user.facebook_id = profile['id']
    user.username = profile['username']
    user.first_name = profile['first_name']
    user.last_name = profile['last_name']
    user.save()
    return user