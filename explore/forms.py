from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class StartupForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['Name','startupName','description','image1','image2','image3','revenue','date','location', 'contact_No']


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        