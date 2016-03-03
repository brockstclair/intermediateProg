# Brock St. Clair
#
# 3/2/16
# Intermediate Programming Lab 6
#
# This class contains the Stack.

class EmptyStack(Exception):
    pass

class Node:

    def __init__(self, data, next = None):
        self._data = data
        self._next = None
        self._precedence = 0

    def ret_data(self):
        return self._data

    def next(self):
        return self._next

    def set_next(self, item):
        self._next = item

class Stack:

    def __init__(self):
        self._tos = None
        self._size = 0

    def push(self, item):
        if self._tos == None:
            self._tos = Node(item)
            self._size += 1
        else:
            new = Node(item)
            new.set_next(self._tos)
            self._tos = new
            self._size += 1

    def pop(self):
        # Checks first to see if there is an item to pop.
        if self._size == 0:
            raise EmptyStack("The stack is empty.")
        else:
            # This holds the node we are popping. This is for the return. It also reduces size by one.
            popData = self._tos
            self._size -= 1

            # This conditional block will check whether there is another item in the list other than
            # the item being popped.
            if self._tos.next() == None:
                self._tos == None
            else:
                self._tos = self._tos.next()

            # Returns the popped node.
            return popData


    def top(self):
        return self._tos.ret_data()

    def size(self):
        sizeCount = 1
        curr = self._tos

        while curr.next() != None:
            sizeCount += 1
            curr = curr.next()

        return sizeCount

    def empty_stack(self):
        if self._size == 0:
            return True
        else:
            return False
