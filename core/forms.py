from django import forms
from .models import User
from django.contrib.auth.forms import AuthenticationForm

# Patient login form
class PatientLoginForm(AuthenticationForm):
    username = forms.CharField(label="Email or Username", widget=forms.TextInput(attrs={
        "class": "w-full border rounded px-4 py-2",
        "placeholder": "Email or Username"
    }))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={
        "class": "w-full border rounded px-4 py-2",
        "placeholder": "Password"
    }))

# Patient registration form
class PatientRegistrationForm(forms.ModelForm):
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={
        "class": "w-full border rounded px-4 py-2",
        "placeholder": "Password"
    }))

    class Meta:
        model = User
        fields = ["username", "email", "phone_number", "password"]
