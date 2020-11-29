from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField

class UserCreateForm ( UserCreationForm ):
    '''
    This class is basically deriving from the form
    already defined in the auth module.
    The base class itself is deriving from ModelForm
    as we can see that the fields and the model is
    being specified in the meta class sub class
    '''
    class Meta:
        model = get_user_model()
        fields = ("username", "email")
        field_classes = {'username': UsernameField,
                         'email' : forms.EmailField }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields["username"].label = "Display name"
        # self.fields[ 'email' ].label = "Email address"
