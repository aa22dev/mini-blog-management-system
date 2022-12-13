import config
import components.posts as posts
import components.feedbacks as feedbacks


class dashboard:
    def mainMenu(self):
        ch = None
        while ch != 'd':
            menu = {
                'a': self.logMenu,
                'b': posts.users.reg,
                'c': self.frontend,
                'd': exit
            }
            print("""a. Login
b. Register
c. Continue as Guest
d. Exit""")
            ch = input("Choose one option: ")
            try:
                menu[ch]()
            except KeyError:
                print("Invalid Option Chosen!")

    def logMenu(self):
        posts.users.login()
        while config.loggedInUser is not None:
            if config.loggedInUser.role == 'Registered':
                menu = {
                    'a': self.frontend,
                    'b': feedbacks.give,
                    'c': posts.users.logout
                }
                print("""a. Frontend
b. Give Feedbacks
c. Logout""")
                ch = input("Choose any one option!")
                try:
                    menu[ch]()
                except KeyError:
                    print("Invalid Option Chosen!")
            else:
                menu = {
                    'a': self.frontend,
                    'b': self.backend,
                    'c': feedbacks.give,
                    'd': posts.users.logout
                }
                print("""a. Frontend
b. Backend
c. Give Feedbacks
d. Logout""")
                ch = input("Choose any one option!")
                try:
                    menu[ch]()
                except KeyError:
                    print("Invalid Option Chosen!")

    def frontend(self):
        ch = None
        while ch != 'd':
            menu = {
                'a': self.posts,
                'b': self.posts_byCategory,
                'c': self.posts_byAuth
            }
            print("""a. All Posts
b. Browse Posts by Categories
c. Browse Posts by Authors
d. Go Back""")
            ch = input("Choose any option: ")
            if ch == 'd':
                return
            try:
                menu[ch]()
            except KeyError:
                print("Invalid Option Chosen!")

    def posts_byCategory(self):
        ch = None
        while ch != 'd':
            print("""a. All Categories
b. Categories by Alphabet
c. Go Back""")
            menu = {
                'a': posts.category.allCat,
                'b': posts.category.showCat_byAlpha
            }
            ch = input("Choose any option: ")
            if ch == 'c':
                return
            try:
                menu[ch]()
            except KeyError:
                print("Invalid Option Chosen!")
            self.posts(1)

    def posts_byAuth(self):
        ch = None
        while ch != 'd':
            print("""a. All Authors
b. Authors by Alphabet
c. Go Back""")
            menu = {
                'a': posts.users.allUsers,
                'b': posts.users.allUsers_byAlpha
            }
            ch = input("Choose any option: ")
            if ch == 'c':
                return
            try:
                menu[ch]()
            except KeyError:
                print("Invalid Option Chosen!")
            self.posts(2)

    @staticmethod
    def posts(op=None):
        t = None
        if op is None:
            posts.allPosts()
        elif op == 1:
            t = posts.posts_byCat()
        else:
            t = posts.post_byAuth()
        if t != -1:
            ch = input("Enter post id to view post or press 0 to go back: ")
            if ch == 0:
                return
            else:
                try:
                    config.data.posts[int(ch)].single()
                except ValueError:
                    raise KeyError
                except KeyError:
                    print("Invalid Post ID Entered!")

    def backend(self):
        ch = None
        while ch != 'f':
            menu = {
                'a': self.postMenu,
                'b': posts.comments.showAll,
                'c': self.catMenu,
                'd': self.userMenu,
                'e': feedbacks.show
            }
            print("""a. Posts
b. Comments
c. Categories
d. Users
e. Feedbacks
f. Go Back""")
            ch = input("Choose any option: ")
            if ch == 'f':
                return
            try:
                menu[ch]()
            except KeyError:
                print("Invalid Option Chosen!")

    def postMenu(self):
        menu = {
            'a': self.allPostBack,
            'b': posts.newPost,
        }
        print("""a. All Posts
b. Add New Post
c. Go Back""")
        ch = input("Choose one option: ")
        if ch == 'c':
            return
        try:
            menu[ch]()
        except KeyError:
            print("Invalid Option Chosen!")

    @staticmethod
    def allPostBack():
        posts.allPosts()
        menu = {
            'a': posts.delete_post,
            'b': posts.modify
        }
        print("""a. Delete Post
b. Edit Post
c. Go Back""")
        ch = input("What action you want to perform: ")
        if ch == 'c':
            return
        try:
            menu[ch]()
        except KeyError:
            print("Invalid Option Chosen!")

    def catMenu(self):
        menu = {
            'a': self.allCatBack,
            'b': posts.category.newCat
        }
        print("""a. All Categories
b. Add New Categories
c. Go Back""")
        ch = input("Choose any option: ")
        if ch == 'c':
            return
        try:
            menu[ch]()
        except KeyError:
            print("Invalid Option Chosen")

    @staticmethod
    def allCatBack():
        posts.category.allCat()
        menu = {
            'a': posts.category.delete_category,
            'b': posts.category.edit
        }
        print("""a. Delete Category
    b. Edit Category
    c. Go Back""")
        ch = input("What action you want to perform: ")
        if ch == 'c':
            return
        try:
            menu[ch]()
        except KeyError:
            print("Invalid Option Chosen!")

    def userMenu(self):
        menu = {
            'a': self.allUserBack,
            'b': posts.users.add_user
        }
        print("""a. All Users
b. Add New User
c. Go Back""")
        ch = input("Choose any option: ")
        if ch == 'c':
            return
        try:
            menu[ch]()
        except KeyError:
            print("Invalid Option Chosen")

    @staticmethod
    def allUserBack():
        posts.users.allUsers()
        menu = {
            'a': posts.users.delete_user,
            'b': posts.users.modify_user,
            'c': posts.users.suspend,
            'd': posts.users.unsuspend
        }
        print("""a. Delete User
b. Edit User
c. Suspend User
d. Unsuspend User
e. Go Back""")
        ch = input("What action you want to perform: ")
        if ch == 'e':
            return
        try:
            menu[ch]()
        except KeyError:
            print("Invalid Option Chosen!")
