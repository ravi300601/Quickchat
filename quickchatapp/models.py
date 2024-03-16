from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    pic = models.ImageField(upload_to="img", blank=True, null=True)
    friends = models.ManyToManyField('Friend', related_name="my_friends")

    def __str__(self):
        return self.name

    def add_friend(self, account):
        """
        Add a new friend
        """
        if not account in self.friend.all():
            self.friends.add(account)

    def remove_friend(self, account):
        """
        Remove a new friend
        """
        if account in self.friend.all():
            self.friends.remove(account)

    def unfriend(self, removee):
        """
        Initiate the action of unfriending soneone
        """
        remover_friends_list = self #person terminating the friendship

        # remove friend from removee_friend_list
        remover_friends_list.remove_friend(removee)
        
        #remove friend from removee friend list
        friend_list = Profile.objects.get(user=removee)
        friend_list.remove_friend(self.user)

    def is_mutual_friend(self,friend):
        """
        Is this a friend?
        """
        if friend in self.friends.all():
            return True
        return False

        
class Friend(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.profile.name
        

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

    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="receiver")
    is_active = models.BooleanField(blank=True, null=False, default=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sender.name

    def accept(self):
        """
        Accept a friend request
        Update both SENDER and RECEIVER friend lists
        """
        breakpoint()
        receiver_friend_list = Profile.objects.get(user=self.receiver)
        if receiver_friend_list:
            receiver_friend_list.add_friend(self.sender)
            sender_friend_list = Profile.objects.get(user=self.sender)
            if sender_friend_list:
                sender_friend_list.add_friend(self.receiver)
                self.is_active = False

    def decline(self):
        """
        It is declined by setting the 'is_active' field to false
        """
        self.is_active = False
        self.save()

    def cancel(self):
        """
        It is cancelled by setting the 'is_active' field to false
        This is only different with respect to "declining" through the notification that is generated.
        """
        self.is_active = False
        self.save()
