import config


class categories:
    def __init__(self):
        self.name = None
        self.cid = None

    def create_category(self):
        self.name = input("Enter the name of category: ")
        self.cid = len(config.data.categories) + 1

    def modify(self):
        self.name = input("Enter new name of category: ")


def edit():
    ch = input("Enter Category ID to edit: ")
    try:
        config.data.categories[int(ch)].modify()
        print("Category Successfully Edited!")
    except KeyError:
        print("Invalid Option Chosen!")


def delete_category():
    print("NOTE: DELETING CATEGORY WILL DELETE ALL THE POSTS ASSOCIATED WITH THAT CATEGORY")
    cid = input("Enter id of category to delete: ")
    try:
        del config.data.categories[int(cid)]
        for key in config.data.posts:
            if config.data.posts[key].cat == int(cid):
                del config.data.posts[key]
    except KeyError:
        print("Invalid Category ID entered!")


def allCat():
    for key in config.data.categories:
        print(f"{key}. {config.data.categories[key].name}")     # dict= {key: value}


def showCat_byAlpha():
    ch = input("Enter any alphabet: ")
    data = config.db.linkedlist.LinkedList()
    for key in config.data.categories:
        if config.data.categories[key].name[0] == ch:
            string = str(key) + '. ' + config.data.categories[key].name
            data.push(string)
    if len(data) != 0:
        print(data)
    else:
        print("No Category Found!")


def newCat():
    c = categories()
    c.create_category()
    config.data.setCategories(c)
    print("Category Created Successfully")
