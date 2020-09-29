from django import forms
from .models import Bug

class bug_creation_form(forms.ModelForm):
    class Meta:
        model=Bug
        fields = "__all__"

class login_form(forms.Form):
    user_name = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput())