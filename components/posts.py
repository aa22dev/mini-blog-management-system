import config
import components.category as category
import components.users as users
import components.comments as comments


class posts:
    def __init__(self):
        self.pid = None
        self.title = None
        self.desc = None
        self.cat = None
        self.username = None

    def create_post(self):
        self.title = input("Enter Post Title: ")
        self.desc = input("Enter Post Description: ")
        category.allCat()
        cat = input("Choose any Category: ")
        if cat not in config.data.categories.keys():
            print("Invalid category ID entered!")
        else:
            self.cat = cat
        self.pid = len(config.data.posts) + 1
        self.username = config.loggedInUser.username

    def modify(self):
        ch = input("""What you want to modify? 
1. Title
2. Description
3. Category
""")
        if ch == '1':
            self.title = input("Enter new Post Title: ")
        elif ch == '2':
            self.desc = input("Enter new Post Description: ")
        elif ch == '3':
            category.allCat()
            cat = input("Choose any new Category: ")
            if cat not in config.data.categories.keys():
                print("Invalid Category ID entered!")
            else:
                self.cat = cat

    def single(self):
        print(f"""Title: {self.title}
Author: {self.username}
Description:
\t\t{self.desc}""")
        if len(config.data.comments[self.pid]) != 0:
            print(f"Comments: \n{config.data.comments[self.pid]}")
        if config.loggedInUser:
            ch = input("Press 1 to post comment and any key to go back: ")
            if ch == '1':
                c = comments.Comments()
                c.create_comment()
                config.data.setComments(c, self.pid)
            else:
                return


def delete_post():
    ch = input("Enter Post ID to delete: ")
    try:
        del config.data.posts[int(ch)]
        print("Post Successfully Deleted!")
    except KeyError:
        print("Invalid Post ID entered!")


def modify():
    ch = input("Enter Post ID to edit: ")
    try:
        config.data.posts[int(ch)].modify()
        print("Post Successfully Edited!")
    except KeyError:
        print("Invalid Option Chosen!")


def allPosts():
    if len(config.data.posts) != 0:
        for key in config.data.posts:   # config.data.posts = {1: "value"}, key = 1
            print(f"{key}. {config.data.posts[key].title}")     # config.data.posts[1].title
    else:
        print("No Record Found!")


def posts_byCat():
    p = config.db.linkedlist.LinkedList()
    ch = input("Enter Category ID: ")
    for key in config.data.posts:
        if config.data.posts[key].cat == int(ch):
            string = str(key) + '. ' + config.data.posts[key].title
            p.push(string)
    if len(p) != 0:
        print(p)
    else:
        print("No Record Found!")
        return -1


def post_byAuth():
    ch = input("Enter Username: ")
    p = config.db.linkedlist.LinkedList()
    for key in config.data.posts:
        if config.data.posts[key].username == ch:
            string = str(key) + '. ' + config.data.posts[key].title
            p.push(string)
    if len(p) != 0:
        print(p)
    else:
        print("No Record Found!")


def newPost():
    p = posts()
    p.create_post()
    config.data.setPosts(p)
    print("Post Successfully Created!")
