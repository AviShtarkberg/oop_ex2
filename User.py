from Exceptions import OnlineError, NoSuchUser, CantFollowYourSelf, CantFollowTwice
from NotificationFactory import NotificationFactory
from Followers import Followers
from PostFactory import *
from Sender import Sender

'''
This class will represent a user in our network.
This class inherits from UserThatNotify and Followers interfaces. 
The inheritance of this 2 class will be the responsible for the implementation 
the observer design pattern.
Important methods of this class:
------------------------------------------------------------------------------
for the observer design pattern:
- follow: will make a user follow another user. will add the user 
to the followers list.
- unfollow: will remove the user from the followers list.
- notify: will notify the user that follows the user after he posts a post.
- update: will be the responsible for adding the notification to the 
    followers of the user. will use the notification factory to generate 
    a new notification for new post of the user. 
------------------------------------------------------------------------------
- publish_post: will use the post factory to generate a new post based on the
    first string that the user will enter that represent the type of the 
    post(text, image or sales). will use the notify method as mentioned above.
- print notification: will iterate the notifications of the user and 
    will print them.
------------------------------------------------------------------------------
This class will use this exceptions:
- OnlineError: if users try to do things while logged out(except getting notifications).
- NoSuchUser: for unfollowing users that you dont follow.
- CantFollowYourSelf.
- CantFollowTwice: you cant follow someone twice.
'''


class Users(Sender, Followers):
    def __init__(self, name, password):
        self.__name = name
        self.__password = password
        self.__isOnline = True
        self.__posts = []
        self.__followers = set()
        self.__notifications = []
        self.__numberOfPosts = 0
        self.__numberOfFollowers = 0

    def get_online(self):
        return self.__isOnline

    def follow(self, otherUser):
        if not self.__isOnline:
            raise OnlineError("you cant post outline")
        if self == otherUser:
            raise CantFollowYourSelf("you cant follow yourself")
        if self in otherUser.__followers:
            raise CantFollowTwice("you can't follow same user twice")
        otherUser.__followers.add(self)
        otherUser.__numberOfFollowers = otherUser.__numberOfFollowers+1
        print(self.__name, "started following", otherUser.__name)

    def unfollow(self, user):
        if not self.__isOnline:
            raise OnlineError("cant unfollow outline")
        if self not in user.__followers:
            raise NoSuchUser("you can't unfollow user you don't follow")
        user.__followers.remove(self)
        user.__numberOfFollowers = user.__numberOfFollowers-1
        print(self.__name + " unfollowed " + user.get_username())

    def logOut(self):
        if not self.__isOnline:
            raise OnlineError("already disconnected")
        self.__isOnline = False

    def logIn(self):
        self.__isOnline = True

    def notify(self):
        for observer in self.__followers:
            observer.update(self)

    def update(self, user):
        notification = NotificationFactory.notification("new_post", user)
        self.add_notification(notification)

    def publish_post(self, type_of_post, *args, **kwargs):
        if not self.__isOnline:
            raise OnlineError("you cant post outline")
        post = PostFactory.write_the_post(type_of_post, *args, **kwargs)
        post.set_user(self)
        self.__posts.append(post)
        self.notify()
        print(post.__str__())
        self.__numberOfPosts = self.__numberOfPosts + 1
        return post

    def get_password(self):
        return self.__password

    def get_username(self):
        return self.__name

    def add_notification(self, notification):
        self.__notifications.append(notification)

    def print_notifications(self):
        if not self.__isOnline:
            raise OnlineError("you cant print notifications outline")
        print(self.__name + "'s notifications:")
        for notification in self.__notifications:
            print(notification.__str__())

    def get_number_of_posts(self):
        return self.__numberOfPosts

    def get_number_of_followers(self):
        return self.__numberOfFollowers

    def __str__(self):
        nop = self.__numberOfPosts
        nof = self.__numberOfFollowers
        return ("User name: " + self.__name + ", Number of posts: " +
                str(nop) + ", Number of followers: " + str(nof))

    def __repr__(self):
        return self.__str__()
