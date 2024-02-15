import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from Exceptions import WrongPasswordError
from PostsAbstractClass import PostsAbstractClass

'''
This file will hold all the posts that we got.
will inherit from PostInterface.
the posts will be created with the factory class that is
seperated from this file.
------------------------------------------------------------------------------
we have 3 types of posts: 
- text post.
- image post: will use the matlib library to show the image.
- sales post.
------------------------------------------------------------------------------
This class will use this exceptions:
- WrongPasswordError: for the sales post - if someone tries to edit
    the post, he need to insert the correct password of him self. 
'''


class ImagePost(PostsAbstractClass):
    def __init__(self, PATH):
        self.__PATH = PATH

    def display(self):
        image = mpimg.imread(self.__PATH)
        plt.imshow(image)
        plt.axis('off')
        plt.show()
        print("Shows picture")

    def __str__(self):
        name = self.get_user().get_username()
        return name + " posted a picture\n"


class TextPost(PostsAbstractClass):
    def __init__(self, text):
        self.__text = text

    def __str__(self):
        name = self.get_user().get_username()
        t = name + " published a post:\n"
        return t + "\"" + self.__text + "\"\n"


class SalePost(PostsAbstractClass):
    def __init__(self, name_of_product, price, city):
        self.__name_of_product = name_of_product
        self.__price = price
        self.__city = city
        self.__isAvailable = True

    def discount(self, n, password):
        if self.get_user().get_password() == password:
            self.__price = self.__price - (n/100*self.__price)
            name = self.get_user().get_username()
            print("Discount on " + name + " product! the new price is: " + str(self.__price))
        else:
            raise WrongPasswordError("the password is incorrect")

    def sold(self, password):
        if self.get_user().get_password() == password:
            self.__isAvailable = False
            print(self.get_user().get_username() + "'s product is sold")
        else:
            raise WrongPasswordError("the password is incorrect")

    def __str__(self):
        t = ""
        if self.__isAvailable is True:
            t = "For sale! "
        else:
            t = "Sold! "
        name = self.get_user().get_username()
        s = name + " posted a product for sale:" + "\n"
        return s + t + self.__name_of_product + ", price: " + str(self.__price) + ", pickup from: " + self.__city + "\n"


