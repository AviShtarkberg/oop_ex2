from Exceptions import InUseError, NotInRangeError, WrongPasswordError, NoSuchUser, OnlineError
from User import Users

''''
This class will represent the social network that we are creating.
The get_social_network() method will be responsible for getting only one 
instance of this class, implementing the singleton design pattern.
Contain also methods to sign up, log in, log out to the network.
------------------------------------------------------------------------------
This class will use this exceptions:
- OneAtATimeError: if the user tried to make more than one social network.
- InUseError: for user names that already exist in the network.
- NotInRangeError: for unavailable passwords in the network.
- WrongPasswordError: if the user trying to log in with a wrong password
- NoSuchUser: if user trying to log in and he is not a registered user
- OnlineError: if the user is logged out.
------------------------------------------------------------------------------
Note that: 
1.in this class we also use a Flyweight like concept for
creating the users while sign up. In this case we check in a 
dictionary(in this terms its like the pattern mentioned above) to check
whether we already sign up a user with the same username/password.
2.The image- image1.jpg is the UML diagram of our project. zoom in to see.
'''


class SocialNetwork:
    __instance = None
    __initialized = False

    def __new__(cls, name):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name):
        if not self.__initialized:
            self.__name = name
            print("The social network", self.__name, "was created!")
            self.__usersNames = {}
            self.__passwords = {}
            self.__users = []
            self.__userToNameDIct = {}
            self.__userNameToPasswordDIct = {}
            self.__initialized = True

    def sign_up(self, name, password):
        if self.__usersNames.get(name) is None:
            if self.__passwords.get(name) is None:
                if len(password) > 8 or len(password) < 4:
                    raise NotInRangeError("you need to choose 4-8 long password")
                else:
                    self.__usersNames[name] = True
                    self.__passwords[password] = True
                    newUser = Users(name, password)
                    self.__users.append(newUser)
                    self.__userToNameDIct[name] = newUser
                    self.__userNameToPasswordDIct[name] = password
                    return newUser
            else:
                raise InUseError("this password already in use")
        else:
            raise InUseError("this user name already in use")

    def log_out(self, user_name):
        user = self.__userToNameDIct.get(user_name)
        user.logOut()
        print(user_name + " disconnected")

    def log_in(self, user_name, password):
        if self.__userToNameDIct.get(user_name) is None:
            raise NoSuchUser("there is no such user")
        if self.__userToNameDIct.get(user_name).get_online() is True:
            raise OnlineError("the user already in")
        user = self.__userToNameDIct.get(user_name)
        usersPassword = self.__userNameToPasswordDIct.get(user_name)
        if usersPassword == password:
            user.logIn()
            print(user_name + " connected")
        else:
            raise WrongPasswordError("the password is incorrect")

    def __str__(self):
        t = self.__name + " social network:\n"
        for user in self.__users:
            t = t + user.__str__() + "\n"
        return t
