from abc import ABC, abstractmethod


class Notification(ABC):

    @abstractmethod
    def __init__(self, user):
        self.__user = user

    def get_user(self):
        return self.__user
