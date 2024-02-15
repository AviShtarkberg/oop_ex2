from Notifications import *

'''
This class will be the responsible for creating the notification object.
Implement the factory design pattern. will create the notification based on the 
type parameter of the installation that is passed into this class.
'''


class NotificationFactory:
    @staticmethod
    def notification(typeOfNotification, user):
        if typeOfNotification == "like":
            return LikeNotification(user)
        if typeOfNotification == "comment":
            return CommentNotification(user)
        if typeOfNotification == "new_post":
            return NewPostNotification(user)
