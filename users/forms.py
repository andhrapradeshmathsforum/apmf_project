from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields =('email','phone_number',)

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email','phone_number',)

