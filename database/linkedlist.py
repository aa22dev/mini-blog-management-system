class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.__head = None
        self.__counter = -1

    def __str__(self):
        d = str(self.__head.data)
        temp = self.__head
        while temp.next is not None:
            temp = temp.next
            d += '\n' + str(temp.data)
        return d

    def __len__(self):
        return self.__counter + 1

    def push(self, data):
        n = Node(data)
        if self.__head is None:
            self.__head = n
        else:
            n.next = self.__head
            self.__head = n
        self.__counter += 1

    def pop(self):
        temp = self.__head
        tempData = self.__head.data
        self.__head = temp.next
        temp.next = None
        temp.data = None
        temp = None
        return tempData
