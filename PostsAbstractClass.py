from abc import ABC, abstractmethod
from Exceptions import OnlineError
from NotificationFactory import NotificationFactory

"""
This class will be an abstract class of the posts.
The main goal of this class is to generalize the different types of posts 
that we allow to post(text, image, sales).
We use this abstract class to avoid recode in each post class.
------------------------------------------------------------------------------
The main methods of this class are:
- like method.
- comment method.
- set user of the post method.
------------------------------------------------------------------------------
This class will use this exceptions:
- OnlineError: if someone tries to like or comment while he is outline.
"""


class PostsAbstractClass(ABC):
    __comments = []
    __user = None
    __likes = 0

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    def get_user(self):
        return self.__user

    def set_user(self, user):
        self.__user = user

    def like(self, user):
        if not self.__user.get_online:
            raise OnlineError("you cant like a post outline")
        if user is not self.__user:
            self.__user.add_notification(NotificationFactory.notification("like", user))
            print("notification to " + self.__user.get_username() + ": " + user.get_username() + " liked your post")
        self.__likes = self.__likes + 1

    def comment(self, user, text):
        if not self.__user.get_online:
            raise OnlineError("you cant comment to a post outline")
        if user is not self.__user:
            self.__user.add_notification(NotificationFactory.notification("comment", user))
            print("notification to " + self.__user.get_username() + ": " + user.get_username() +
                  " commented on your post: " + text)
        self.__comments.append(text)
