# How to construct attributes in class---------------
# class User:
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#
#
# user_1 = User("001", "vickydarlinn")
# user_2 = User("002", "antilaman")
#
#
# print(user_1.username)

# how to add method in a class------------------------
# class User:
#     def __init__(self, user_id, username):
#         self.id = user_id
#         self.username = username
#         self.followers = 0
#         self.followings = 0
#
#     def follow(self,user):
#         self.followings += 1
#         user.followers += 1
#
#
# user_1 = User("001","vickydarlinn")
# user_2 = User("002", "antilaman")
#
# user_1.follow(user_2)
# print(user_1.followers)
# print(user_1.followings)
# print(user_2.followers)
# print(user_2.followings)

