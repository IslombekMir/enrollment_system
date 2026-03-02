from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models import User

class SignUpForm(UserCreationForm):
    class Meta:
        model = User ### removing role
        fields = ("username", "email", "password1", "password2")