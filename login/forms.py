from django import forms
from .models import login

class LoginForm(forms.ModelForm):
    class Meta:
        model = login
        fields = "__all__"