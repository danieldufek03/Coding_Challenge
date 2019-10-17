from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User, Organization

class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = User
        fields = ('email', 'first_name', 'last_name', 'address', 'phone', 'organizations')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'address', 'phone', 'organizations')
