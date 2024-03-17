from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from .models import ChatMessage

class UserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter firstname'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter lastname'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm username'}))
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "password1", "password2"]

class ChatMessageForm(ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={"id":"msg_id", "class":"form-control", "rows": 1, "type":"text", "placeholder":"Type..."}))
    class Meta:
        model = ChatMessage
        fields = ["body",]
