from django.shortcuts import render, redirect
from .models import Profile, Friend, ChatMessage, FriendRequest, Notification
from django.contrib.auth import authenticate, login, logout, get_user_model
from .forms import ChatMessageForm, UserForm, ProfileForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
import json

# Create your views here.
@login_required(login_url="login")
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

def register(request):
    if request.user.is_authenticated:
        return redirect("index")
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")
    context={"form": form}
    return render(request,"quickchatapp/register.html", context)

def signin(request):
    if request.user.is_authenticated:
        return redirect("index")
    error_msg = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("index")
        else:
            error_msg = "Invalid Credentials"
    context={"msg": error_msg}
    return render(request,"quickchatapp/login.html", context)

def signout(request):
    logout(request)
    return redirect("login")

@login_required(login_url='login')
def update_profile(request):
    user = request.user
    profile = Profile.objects.get(user=user)
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("update_profile")
    context = {"form": form}
    return render(request, "quickchatapp/update_profile.html", context)

@login_required(login_url='login')
def friend_request(request):
    user = request.user
    friend_requests = FriendRequest.objects.filter(receiver = user)
    context = {"f_requests": friend_requests}
    return render(request, "quickchatapp/friend_request.html", context)

def accept_friend_request(request):
    id = json.loads(request.body)
    user_id = id
    user = get_user_model()
    n_user = user.objects.get(id=user_id)
    profile = Profile.objects.get(user_id=request.user.id)
    profile2 = Profile.objects.get(user_id=user_id)
    f_requests = FriendRequest.objects.get(sender=n_user, receiver=request.user)
    msg = None
    if profile:
        if profile.friends.filter(id=user_id).exists():
            profile.friends.remove(n_user)
            msg = "no"
        else:
            profile.friends.add(n_user)
            f_requests.delete()
            notification = Notification.objects.create(sender=request.user, receiver=n_user,
                                                        description=f"Hi, {request.user.username} accepted your friend request.")
            msg="yes"
        if not Friend.objects.filter(profile_id=profile.id).exists():
            Friend.objects.create(profile_id=profile.id)
    if profile2:
        if profile2.friends.filter(id=request.user.id).exists():
            profile2.friends.remove(request.user)
        else:
            profile2.friends.add(request.user)
        if not Friend.objects.filter(profile_id=profile2.id).exists():
            Friend.objects.create(profile_id=profile2.id)
    return JsonResponse(msg, safe=False)

@login_required(login_url='login')
def suggestion(request):
    all_user = get_user_model()
    user = request.user
    profile = Profile.objects.get(user=user)
    profile_friends = profile.friends.all()
    suggested_friends = all_user.objects.exclude(profile__friends__in = profile_friends).exclude(profile=profile)
    friend_requests = FriendRequest.objects.filter(receiver__in = suggested_friends, sender = request.user)
    context = {"s_friends": suggested_friends, "f_friend": friend_requests}
    return render(request, "quickchatapp/suggestion.html", context)

def send_friend_request(request):
    data = json.loads(request.body)
    user = get_user_model()
    receiver = user.objects.get(id = data)
    friend_request = FriendRequest.objects.create(sender=request.user, receiver=receiver)
    return JsonResponse("it is going", safe=False)

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
