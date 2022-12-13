import config


class Comments:
    def __init__(self):
        self.cid = None
        self.username = None
        self.comment = None

    def create_comment(self):
        self.cid = len(config.data.comments) + 1
        self.username = config.loggedInUser.username
        self.comment = input("Enter Comment: ")

    def __str__(self):
        return f"""\t\tComment By: {self.username}
\t\tComment: {self.comment}"""


def showAll():
    for key in config.data.comments:
        print(f"\n{config.data.comments[key]}")
