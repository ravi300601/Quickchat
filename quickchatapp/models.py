from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    pic = models.ImageField(upload_to="img", blank=True, null=True)
    friends = models.ManyToManyField(User, related_name="my_friends", blank=True)

    def __str__(self):
        return self.username

    # def add_friend(self, account):
    #     """
    #     Add a new friend
    #     """
    #     if not account in self.friend.all():
    #         self.friends.add(account)

    # def remove_friend(self, account):
    #     """
    #     Remove a new friend
    #     """
    #     if account in self.friend.all():
    #         self.friends.remove(account)

    # def unfriend(self, removee):
    #     """
    #     Initiate the action of unfriending soneone
    #     """
    #     remover_friends_list = self #person terminating the friendship

    #     # remove friend from removee_friend_list
    #     remover_friends_list.remove_friend(removee)
        
    #     #remove friend from removee friend list
    #     friend_list = Profile.objects.get(user=removee)
    #     friend_list.remove_friend(self.user)

    # def is_mutual_friend(self,friend):
    #     """
    #     Is this a friend?
    #     """
    #     if friend in self.friends.all():
    #         return True
    #     return False

        
class Friend(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.profile.username
        

class ChatMessage(models.Model):
    body = models.TextField()
    msg_sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="msg_sender")
    msg_receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="msg_receiver")
    seen = models.BooleanField(default=False)

    def __str__(self):
        return self.body

class FriendRequest(models.Model):
    """
    A friend request consists of two main parts:
        1. SENDER:
            Person sending the friend request
        2. RECEIVER:
            Person receiving the friend request
    """

    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_requests")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_request")
    seen = models.BooleanField(blank=True, null=False, default=False)

    def __str__(self):
        return f"{self.sender.username} sent {self.receiver.username} a friend request"

class Notification(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender_notification")
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver_notification")
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    seen = models.BooleanField(default=False)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"Hi {self.sender.username} accepted your friend request"
