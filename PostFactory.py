from abc import ABC
from Posts import *
from PostsAbstractClass import PostsAbstractClass

'''
This class will be the responsible for creating the posts object.
Implement the factory design pattern. will create the posts based on the 
type the the user enters as the first parameter of the installation.
'''


class PostFactory(PostsAbstractClass, ABC):
    @staticmethod
    def write_the_post(type_of_post,  *args, **kwargs):
        if type_of_post == "Text":
            return TextPost(*args)
        if type_of_post == "Sale":
            return SalePost(*args, **kwargs)
        if type_of_post == "Image":
            return ImagePost(*args)

