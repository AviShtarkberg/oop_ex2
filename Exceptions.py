"""
this class will contain all the exceptions that we will use in this project.
"""


class WrongPasswordError(Exception):
    pass


class InUseError(Exception):
    pass


class NotInRangeError(Exception):
    pass


class OnlineError(Exception):
    pass


class NoSuchUser(Exception):
    pass


class CantFollowYourSelf(Exception):
    pass


class CantFollowTwice(Exception):
    pass
