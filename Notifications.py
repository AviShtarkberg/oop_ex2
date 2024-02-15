from NotificationInterface import Notification

'''
This file will hold all the notifications that we got.
will inherit from NotificationInterface.
the notifications will be created with the factory class that is
seperated from this file.
------------------------------------------------------------------------------
we have 3 types of notifications: 
- comment notification.
- like notification.
- new post notification: this notification need to be send to all users followers.
'''


class CommentNotification(Notification):
    def __init__(self, user):
        super().__init__(user)

    def __str__(self):
        t = " commented on your post"
        return self.get_user().get_username() + t


class NewPostNotification(Notification):
    def __init__(self, user):
        super().__init__(user)

    def __str__(self):
        t = " has a new post"
        return self.get_user().get_username() + t


class LikeNotification(Notification):
    def __init__(self, __user):
        super().__init__(__user)

    def __str__(self):
        t = " liked your post"
        return self.get_user().get_username() + t
