import unittest
from Exceptions import *
from SocialNetwork import SocialNetwork

'''
This class is responsible for testing the code with unit test.
The main goal of this class is to check the things that are not checked in 
the main class that was provided.
Thus we will test almost only the functionality of the Exception class and the
situations where things got wrong.
'''


class Tests(unittest.TestCase):
    # tests that there is only one net at a time:
    def test_only_one_net(self):
        network = SocialNetwork("Twitter")
        network2 = SocialNetwork("M")
        u1 = network.sign_up("Alice", "pass1")
        u2 = network2.sign_up("Bob", "pass2")
        self.assertEqual(print(network), print(network2))

    # tests that the username used only once.
    def test_one_username(self):
        network = SocialNetwork("Twitter")
        network.sign_up("alice", "aaaa")
        with self.assertRaises(InUseError):
            network.sign_up("alice", "11111")
        with self.assertRaises(InUseError):
            network.sign_up("alice", "aaaa")

    # tests that the password is 4-8 chars.
    def test_in_range_password(self):
        network = SocialNetwork("Twitter")
        with self.assertRaises(NotInRangeError):
            network.sign_up("alice", "1")
        with self.assertRaises(NotInRangeError):
            network.sign_up("alice", "111111111111111")

    # test that users can be active only while logged in.
    # will test also that user don't get notification for him self likes/ comments
    def test_only_online(self):
        network = SocialNetwork("Twitter")
        u1 = network.sign_up("abby", "1234")
        u2 = network.sign_up("boby", "4321")
        p2 = u1.publish_post("Image", 'image1.jpg')
        u1.logOut()
        with self.assertRaises(OnlineError):
            u1.logOut()
            u1.follow(u2)
            u1.publish_post("Text", "alice")
            u1.unfollow()
            p2.like(u1)
            p2.comment(u1)
        p2.like(u2)
        p2.like(u1)
        p2.comment(u1, "hhh")
        network.log_in("abby", "1234")
        # will check that we still get notifications while outline.
        # don't get your self notifications for likes and comments.
        u1.print_notifications()

    # test that user cant follow another user twice
    def test_one_follow(self):
        network = SocialNetwork("Twitter")
        u1 = network.sign_up("ray", "4444")
        u2 = network.sign_up("tay", "6666")
        u1.follow(u2)
        with self.assertRaises(CantFollowTwice):
            u1.follow(u2)

    # test that you cant follow your self
    def test_follow_yourself(self):
        network = SocialNetwork("Twitter")
        u1 = network.sign_up("may", "44441")
        with self.assertRaises(CantFollowYourSelf):
            u1.follow(u1)

    # will check that the sales posts working correctly
    def test_sale_post(self):
        network = SocialNetwork("Twitter")
        u1 = network.sign_up("mel", "r1234")
        p3 = u1.publish_post("Sale", "Toyota prius 2012", 42000, "Haifa")
        with self.assertRaises(WrongPasswordError):
            p3.discount(10, "2222")
            p3.sold("2222")

