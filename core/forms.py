# core/forms.py
from django import forms
from .models import User

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role', 'phone_number', 'occupation']
        widgets = {
            'password': forms.PasswordInput(),
        }
