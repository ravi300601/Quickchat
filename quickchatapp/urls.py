from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('register', views.register, name="register"),
    path('login', views.signin, name="login"),
    path('logout', views.signout, name="logout"),
    path('friends/<str:pk>', views.details, name="details"),
    path('sent_msg/<str:pk>', views.sentMessages, name="sent_msg"),
    path('rev_msg/<str:pk>', views.receivedMessages, name="rev_msg"),
    path('notification', views.chatNotification, name="notification"),
    path('test/<str:pk>', views.sentFriendRequests, name="requests")
]
