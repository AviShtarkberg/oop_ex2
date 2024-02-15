from abc import ABC, abstractmethod

'''
This class is an abstract class that represent the user that 
will send the notification that he is posted a new post.
The explanation of this class functions is in the User class.
'''


class Sender(ABC):

    @abstractmethod
    def follow(self, user):
        pass

    @abstractmethod
    def unfollow(self, user):
        pass

    @abstractmethod
    def notify(self):
        pass
