from user import User
from post import Post

niki = User("Niki", "niki@abv.bg", "pwd123", "Dev")
niki.get_user_info()
post = Post("Niki", "Some message")
post.get_post_info()