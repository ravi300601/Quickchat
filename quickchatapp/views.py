from django.shortcuts import render, redirect
from .models import Profile, Friend, ChatMessage
from .forms import ChatMessageForm
from django.http import JsonResponse
import json

# Create your views here.
def index(request):
    user = request.user.profile
    friends = user.friends.all()
    context={"user": user, "friends": friends}
    return render(request, "quickchatapp/index.html", context)

def details(request, pk):
    friend = Friend.objects.get(profile_id=pk)
    user = request.user.profile
    profile = Profile.objects.get(id = friend.profile.id)
    friends = user.friends.all()
    chats = ChatMessage.objects.all()
    receiveChats = ChatMessage.objects.filter(msg_receiver=user, msg_sender=profile)
    receiveChats.update(seen=True)
    form = ChatMessageForm()
    if request.method == "POST":
        form = ChatMessageForm(request.POST)
        if form.is_valid():
            chat_message = form.save(commit=False)
            chat_message.msg_sender = user
            chat_message.msg_receiver = profile
            chat_message.save()
            return redirect("details", pk=friend.profile.id)
    context={"friend": friend, 
            "user": user, 
            "profile": profile, 
            "friends": friends, 
            "form": form,
            "chats": chats,
            "chatCounts": receiveChats.count()}
    return render(request, "quickchatapp/details.html", context)

def sentMessages(request, pk):
    user = request.user.profile
    friend = Friend.objects.get(profile_id=pk)
    profile = Profile.objects.get(id=friend.profile.id)
    data = json.loads(request.body)
    new_chat = data["msg"]
    new_chat_message = ChatMessage.objects.create(body=new_chat, msg_sender=user, msg_receiver=profile, seen=False)
    return JsonResponse(new_chat_message.body, safe=False)

def receivedMessages(request, pk):
    user = request.user.profile
    friend = Friend.objects.get(profile_id=pk)
    profile = Profile.objects.get(id=friend.profile.id)
    arr = []
    chats = ChatMessage.objects.filter(msg_receiver=user, msg_sender=profile)
    chats.update(seen=True)
    for chat in chats:
        arr.append(chat.body)
    return JsonResponse(arr, safe=False)

def chatNotification(request):
    user = request.user.profile
    friends = user.friends.all()
    arr = []
    for friend in friends:
        chats = ChatMessage.objects.filter(msg_sender=friend.profile.id, msg_receiver=user, seen=False)
        arr.append(chats.count())
    return JsonResponse(arr, safe=False)
