from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm as UserForm
from django.contrib.auth import get_user_model


class UserCreationForm(UserForm):
    class Meta:
        model = get_user_model()
        fields = ("email", "password1", "password2")


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = forms.EmailInput(
            attrs={'placeholder': 'Email',
                   'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'placeholder': 'Password',
                                                     'class': 'form-control'})
