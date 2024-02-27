from django import forms
from django.forms import ModelForm
from .models import ChatMessage

class ChatMessageForm(ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={"id":"msg_id", "class":"form-control", "rows": 1, "type":"text", "placeholder":"Type..."}))
    class Meta:
        model = ChatMessage
        fields = ["body",]
