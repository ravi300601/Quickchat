from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm
from .models import ChatMessage, Profile

class UserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control', 'aria-label': 'Username', 'aria-describedby': 'username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control', 'aria-label': 'Firstname', 'aria-describedby': 'firstname'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control', 'aria-label': 'Lastname', 'aria-describedby': 'lastname'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control', 'aria-label': 'Password', 'aria-describedby': 'password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password Confirm', 'class': 'form-control', 'aria-label': 'Cpassword', 'aria-describedby': 'CPassword'}))
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "password1", "password2"]

class ProfileForm(ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control', 'aria-label': 'Username', 'aria-describedby': 'username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control', 'aria-label': 'Firstname', 'aria-describedby': 'firstname'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control', 'aria-label': 'Lastname', 'aria-describedby': 'lastname'}))
    # pic = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'upload image', 'class': 'form-control', 'aria-label': 'Picture', 'aria-describedby': 'picture', 'type': 'file'}))

    class Meta:
        model = Profile
        fields = ["username", "first_name", "last_name", "pic"]

class ChatMessageForm(ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={"id":"msg_id", "class":"form-control", "rows": 1, "type":"text", "placeholder":"Type..."}))
    class Meta:
        model = ChatMessage
        fields = ["body",]
