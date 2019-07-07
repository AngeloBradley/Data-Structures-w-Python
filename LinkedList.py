import sys
from Node import Node

class LinkedList:
    def __init__(self):
        self.headval = None
        self.tailval = None
        self.length = 0
        self.empty = True

    def count(self, num):
        pointer1 = self.headval
        count = 0

        while pointer1 is not None:
            if pointer1.dataval == num:
                count += 1
            pointer1 = pointer1.nextval
        return count

    def decreaselength(self):
        self.length -= 1

    def get_nth(self, num):
    
        if num >= self.length:
            return -1

        pointer1, pointer2 = self.init_pointers()

        for _ in range(num):
            pointer1, pointer2 = self.update_pointers(pointer1, pointer2)

        return pointer2.dataval

    def increaselength(self):
        self.length += 1

    def init_pointers(self):
        pointer1 = self.headval
        pointer2 = pointer1

        return pointer1, pointer2

    def peek_first(self):
        return self.headval.dataval
    
    def peek_last(self):
        return self.tailval.dataval

    def printlist(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def set_headval_for_empty_list(self, newdata):
        if newdata.__class__.__name__ == 'Node':
            new_node = newdata
        else:
            new_node = Node(newdata)
        self.headval = new_node
        self.tailval = self.headval
        self.empty = False
        self.increaselength()
        return new_node

    def update_pointers(self, pointer1, pointer2):
        pointer2 = pointer1
        pointer1 = pointer1.nextval

        return pointer1, pointer2
       

if __name__ == '__main__':
    pass