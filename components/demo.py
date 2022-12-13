import config
import components.category as category
import components.users as users
import components.comments as comments
import components.posts as posts
import components.feedbacks as feedbacks


class demo:
    def __init__(self):
        self.users = users.User()
        self.cat = category.categories()
        self.posts = posts.posts()
        self.com = comments.Comments()
        self.feed = feedbacks.Feedback()

    def make(self):
        # Creating Admin user
        self.users.username = "admin"
        self.users.name = "Group no. 1"
        self.users.password = "group_1"
        self.users.status = 'Active'
        self.users.role = 'Admin'
        self.users.demoUser_setPass()

        # Creating General Category
        self.cat.name = "General"
        self.cat.cid = len(config.data.categories) + 1

        # Creating Demo Post
        self.posts.title = "Demo Post"
        self.posts.desc = """Lorem Ipsum Dolar sit amet. Amet Dolar Lorem Sit, Lorem Ipsum Dolar sit amet"""
        self.posts.cat = 1
        self.posts.pid = len(config.data.posts) + 1
        self.posts.username = "admin"

        # Creating Demo Comment
        self.com.cid = len(config.data.comments) + 1
        self.com.username = "admin"
        self.com.comment = "This is a test comment"

        # Creating Demo Feedback
        self.feed.name = "admin"
        self.feed.feedback = "Test Feedback"

        config.data.setUsers(self.users)
        config.data.setCategories(self.cat)
        config.data.setPosts(self.posts)
        config.data.setComments(self.com, 1)
        config.data.setFeedbacks(self.feed)
