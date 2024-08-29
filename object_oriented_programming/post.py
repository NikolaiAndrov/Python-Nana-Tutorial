class Post:
    def __init__(self, author, message):
        self.author = author
        self.message = message

    def get_post_info(self):
        print(f"Author: {self.author}, message: {self.message}.")