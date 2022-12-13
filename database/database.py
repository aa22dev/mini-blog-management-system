import database.linkedlist as linkedlist


class Database:
    def __init__(self):
        self.users = {}
        self.categories = {}
        self.posts = {}
        self.comments = {}
        self.feedbacks = linkedlist.LinkedList()

    def setUsers(self, obj):
        if obj.username not in self.users.keys():
            self.users[obj.username] = obj
            print("Registration Successful")
        else:
            print("User already exists!")

    def setCategories(self, obj):
        if obj.cid not in self.categories.keys():
            self.categories[obj.cid] = obj

    def setPosts(self, obj):
        if obj.pid not in self.posts.keys():
            self.posts[obj.pid] = obj

    def setComments(self, obj, pid):
        if pid not in self.comments.keys():
            d = linkedlist.LinkedList()
            d.push(obj)
            self.comments[pid] = d
        else:
            self.comments[pid].push(obj)

    def setFeedbacks(self, obj):
        self.feedbacks.push(obj)

    def getFeedback(self):
        return self.feedbacks
