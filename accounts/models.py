from django.db import models
from django.contrib import auth

# Create your models here.
class User( auth.models.User, auth.models.PermissionsMixin) :
    '''
    This class is just extending the django built in auth model
    '''
    def __str__():
       return "@{}".format(self.username)
