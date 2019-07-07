from LinkedList import LinkedList
from Node import Node
import sys

class DLinkedList(LinkedList):
    def __init__(self):
        LinkedList.__init__(self)

    #==================================#Private Helper Functions#==================================
    
    def init_pointers_tail(self):
        pointer1 = self.tailval
        pointer2 = pointer1

        return pointer1, pointer2

    def insertion_handler(self, newdata, pointer1, pointer2):
        new_node = Node(newdata)
        new_node.nextval = pointer1
        new_node.previousval = pointer2
        
        pointer1.previousval = new_node
        pointer2.nextval = new_node

        self.increaselength()

    def remove_head(self):
        if self.empty:
            return -1

        if self.length == 1:
            try:
                self.headval.nextval.previousval = None
                sys.exit('remove_head: list has length of 1 but contains more than one node')
            except:
                pass

            try:
                self.headval.previousval.nextval = None
                sys.exit('remove_head: designated head node is not the first node in the list')
            except:
                pass
            
            self.headval.nextval = None
            self.headval.previousval = None
            self.headval = None

        else:
            current_head = self.headval
            new_head = self.headval.nextval

            new_head.previousval = None
            self.headval = new_head

            current_head.nextval = None
            current_head = None

        self.decreaselength()

    def remove_tail(self):

        try:
            self.tailval.nextval.previousval = None
            sys.exit('remove_tail: tail is not the last node in the list')
        except:
            pass

        if self.length == 1:
            self.remove_head()
            self.tailval = None
        else:
            current_tail = self.tailval
            new_tail = self.tailval.previousval

            new_tail.nextval = None
            self.tailval = new_tail

            current_tail.previousval = None
            current_tail = None

        self.decreaselength()

    def update_pointers_reverse(self, pointer1, pointer2):
        pointer2 = pointer1
        pointer1 = pointer1.previousval

        return pointer1, pointer2

    #==================================#Public Functions#==================================
    def prepend(self, newdata):

        if self.empty:
            self.set_headval_for_empty_list(newdata)
        else:
            new_node = Node(newdata)
            new_node.nextval = self.headval
            self.headval.previousval = new_node
            self.headval = new_node
            self.increaselength()

    def append(self, newdata):

        if self.headval == None:
            self.set_headval_for_empty_list(newdata)
        else:
            new_node = Node(newdata)
            self.tailval.nextval = new_node
            new_node.previousval = self.tailval
            self.tailval = new_node
            self.increaselength()

    def insert_ordered(self, newdata, code = 0):

        if self.empty:
            self.set_headval_for_empty_list(newdata)
    
        #code == 0 for ascending and 1 for descending
        if code not in (0, 1):
            sys.exit('incorrect code value passed to remove function')

        if code == 0:
            pointer1, pointer2 = self.init_pointers()

            while pointer1 is not None:

                if pointer1.dataval > newdata:
                    if pointer1 == self.headval:
                        self.prepend(newdata)
                        return
                    self.insertion_handler(newdata, pointer1, pointer2)
                    return
                pointer1, pointer2 = self.update_pointers(pointer1, pointer2)
        
        if code == 1:
            pointer1, pointer2 = self.init_pointers()

            while pointer1 is not None:
                if pointer1.dataval < newdata:
                    if pointer1 == self.headval:
                        self.prepend(newdata)
                        return
                    self.insertion_handler(newdata, pointer1, pointer2)
                    return
                pointer1, pointer2 = self.update_pointers(pointer1, pointer2)

        self.append(newdata)
        return


    def remove(self, dataval, code = 0):
        #code = 0 removes first instance from the left
        #code = 1 removes all instances
        #code = 2 removes first instance from the right
        
        if self.empty:
            return -1
        
        if code not in (0,1,2):
            sys.exit('incorrect code value passed to remove function')

        if code == 0:
            pointer1, pointer2 = self.init_pointers()

            while pointer1 is not None:
                if pointer1.dataval == dataval:
                    if pointer1 == self.headval:
                        self.remove_head()
                        return
                    if pointer1 == self.tailval:
                        self.remove_tail()
                        return
                    pointer2.nextval = pointer1.nextval
                    pointer1.nextval.previousval = pointer2

                    pointer1.nextval = None
                    pointer1.previousval = None
                    self.decreaselength()
                    return

                pointer1, pointer2 = self.update_pointers(pointer1, pointer2)

        if code == 1:
            pointer1, pointer2 = self.init_pointers()

            while pointer1 is not None:
                if pointer1.dataval == dataval:
                    if pointer1 == self.headval:
                        #because p1 and p2 are both pointing to the node
                        #that is due to be removed, you need to first move
                        #both of them to what will become the new head
                        pointer1 = pointer1.nextval
                        pointer2 = pointer1
                        self.remove_head()
                        continue
                    if pointer1 == self.tailval:
                        self.remove_tail()
                        pointer1 = pointer2
                        continue
                    pointer2.nextval = pointer1.nextval
                    pointer1.nextval.previousval = pointer2

                    pointer1.nextval = None
                    pointer1.previousval = None
                    pointer1 = pointer2
                    
                    self.decreaselength()

                pointer1, pointer2 = self.update_pointers(pointer1, pointer2)

        if code == 2:
            pointer1, pointer2 = self.init_pointers_tail()

            while pointer1 is not None:
                if pointer1.dataval == dataval:
                    if pointer1 == self.headval:
                        self.remove_head()
                        return
                    if pointer1 == self.tailval:
                        self.remove_tail()
                        return
                    pointer2.previousval = pointer1.previousval
                    pointer1.previousval.nextval = pointer2

                    pointer1.nextval = None
                    pointer1.previousval = None

                    self.decreaselength()
                    return

                pointer1, pointer2 = self.update_pointers_reverse(pointer1, pointer2)