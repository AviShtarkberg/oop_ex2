from abc import ABC, abstractmethod

'''
This class is an abstract class to represent the follower of a user.
This class is mainly made to implement the observer for the notifications.
The explanation of the update function is in the User class.
'''


class Followers(ABC):
    @abstractmethod
    def update(self, user):
        pass
