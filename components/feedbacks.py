import config


class Feedback:
    def __init__(self):
        self.name = None
        self.feedback = None

    def giveFeedback(self):
        self.name = config.loggedInUser.username
        self.feedback = input("Enter Feedback: ")

    def __str__(self):
        return f"""\t\tFeedback by: {self.name}
\t\tFeedback: {self.feedback}"""


def show():
    print(config.data.getFeedback())


def give():
    f = Feedback()
    f.giveFeedback()
    config.data.setFeedbacks(f)
    print("Feedback submitted successfully!")
