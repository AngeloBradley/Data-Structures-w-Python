from LinkedList import LinkedList
from Node import Node
import sys

class SLinkedList(LinkedList):
    def __init__(self):
        LinkedList.__init__(self)

    #==================================#Private Helper Functions#==================================

    def insertion_handler(self, newdata, pointer1, pointer2):
        #pointer1 is 1 step in front of where the new node belongs
        #pointer2 is 1 step behind where the new node belongs
        new_node = Node(newdata)
        new_node.nextval = pointer1
        pointer2.nextval = new_node

        self.increaselength()

    def remove_head(self):
        if self.empty:
            return -1

        if self.length == 1:
            current_head = self.headval
            current_head.nextval = None #current_head broken away from list
            
            self.empty = True
            self.headval = None
            self.tailval = None
        else:
            current_head = self.headval
            new_head = self.headval.nextval

            current_head.nextval = None #current_head broken away from list
            self.headval = new_head #new_head formally established

        self.decreaselength()
            

        return current_head

    def remove_tail(self):
        if self.empty:
            return -1

        if self.length == 1:
            #in this scenario the head and the tail are the same node
            current_tail = self.remove_head() 
            self.empty = True
            self.headval = None
            self.tailval = None
        else:
            
            pointer1, pointer2 = self.init_pointers()
            #using pointer1.nextval so that when the loop exits
            #pointer1 is on the last node and pointer2 (new_tail)
            #is on the second to last node
            while pointer1.nextval is not None:
                pointer1, pointer2 = self.update_pointers(pointer1, pointer2)

            current_tail = self.tailval
            new_tail = pointer2

            new_tail.nextval = None #current_tail officially broken away from list
            self.tailval = new_tail #new tail formally established

        self.decreaselength()
        return current_tail

    #==================================#Public Functions#==================================
    def alternating_split(self):
        list1 = SLinkedList()
        list2 = SLinkedList()

        for i in range(self.length):
            if i % 2 == 0:
                list1.append(self.remove_head())
            else:
                list2.append(self.remove_head())

        return list1, list2
    
    def append(self, newdata):
        
        if self.empty:
            return self.set_headval_for_empty_list(newdata)
        else:
            if newdata.__class__.__name__ == 'Node':
                new_node = newdata
            else:
                new_node = Node(newdata)
            self.tailval.nextval = new_node
            self.tailval = new_node
            self.increaselength()
            return new_node

    def append_list(self, list2):
        self.length += list2.length

        if self.empty:
            self.headval = list2.headval
            self.tailval = list2.tailval
        else:
            self.tailval.nextval = list2.headval
            self.tailval = list2.tailval

        list2.headval = None
        list2.tailval = None
        list2 = None

    def deep_copy(self):
        copy = SLinkedList()

        pointer1, pointer2 = self.init_pointers()

        while pointer1 is not None:
            copy.append(pointer1.dataval)
            pointer1, pointer2 = self.update_pointers(pointer1, pointer2)

        return copy

    def deletelist(self):

        while self.headval is not None:
            self.remove_head()

        return self.headval, self.tailval, self.length, self.empty

    def frontbacksplit(self):
        backsplit = SLinkedList()

        if self.length < 2:
            return backsplit

        pointer1, pointer2 = self.init_pointers()
        mid = 0

        if self.length % 2 == 0:
            mid = int(self.length / 2)
        else:
            mid = int((self.length // 2) + 1)

        for i in range(mid):
            pointer1, pointer2 = self.update_pointers(pointer1, pointer2)

        #pointer1 is at the head of the backsplit
        #pointer2 is at the tail of the frontsplit

        backsplit.headval = pointer1
        backsplit.tailval = self.tailval
        backsplit.empty = False

        self.tailval = pointer2
        self.tailval.nextval = None

        return backsplit

    def insert_nth(self, index, newdata):
        if index > self.length:
            return -1
        elif index == 0:
            return self.prepend(newdata)
        elif index == self.length:
            return self.append(newdata)
        else:
            pointer1, pointer2 = self.init_pointers()

            for _ in range(index):
                pointer1, pointer2 = self.update_pointers(pointer1, pointer2)

            #pointer1 is pointing to index after the desired location
            #pointer2 is pointing to the index before

            if newdata.__class__.__name__ == 'Node':
                new_node = newdata
            else:
                new_node = Node(newdata)

            pointer2.nextval = new_node
            new_node.nextval = pointer1
            self.increaselength()


        return new_node

    def insert_sort(self):
        new_list = SLinkedList()

        for _ in range(self.length):
            reinsertion_data = self.remove_head().dataval
            new_list.ordered_insert(reinsertion_data)

        self.headval = new_list.headval

    def merge_sort(self):
        pass

    def move_node(self, list2):
        move_this_node = list2.remove_head()
        self.prepend(move_this_node)

    def ordered_insert(self, newdata, code = 0):
        
        if self.empty:
            new_node = self.set_headval_for_empty_list(newdata)
            return new_node

        #code == 0 for ascending and 1 for descending
        if code not in (0,1):
            sys.exit('invalid code value')

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
            
        #this line simply adds the new node to the end if there are no values in the list
        #by which to add the node in ascending (all values are smaller) or descending (all values are larger)
        self.append(newdata)
        return

    def pop(self):
        return self.remove_head().dataval

    def prepend(self, newdata):

        if self.empty:
            return self.set_headval_for_empty_list(newdata)
        else:
            if newdata.__class__.__name__ == 'Node':
                new_node = newdata
            else:
                new_node = Node(newdata)
            new_node.nextval = self.headval
            self.headval = new_node
            self.increaselength()
            return new_node

    def push(self, newdata):
        self.append(newdata)

    def remove(self, data, code = 0):
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
                if pointer1.dataval == data:
                    if pointer1 == self.headval:
                        removed_node = self.remove_head()
                    elif pointer1 == self.tailval:
                        removed_node = self.remove_tail()
                    else:
                        removed_node = pointer1
                        pointer2.nextval = removed_node.nextval
                        removed_node.nextval = None
                        self.decreaselength()
                    
                    if self.length == 0: self.empty = True
                    return removed_node

                pointer1, pointer2 = self.update_pointers(pointer1, pointer2)

            return None
        
        if code == 1:
            pointer1, pointer2 = self.init_pointers()

            while pointer1 is not None:
                if pointer1.dataval == data:
                    if pointer1 == self.headval:
                        #because p1 and p2 are both pointing to the node
                        #that is due to be removed, you need to first move
                        #both of them to what will become the new head
                        pointer1, pointer2 = self.update_pointers(pointer1, pointer2)
                        removed_node = self.remove_head()
                        continue
                    if pointer1 == self.tailval:
                        removed_node = self.remove_tail()
                        pointer1 = pointer2
                        continue
                    
                    removed_node = pointer1
                    pointer2.nextval = removed_node.nextval
                    p1 = removed_node.nextval #ensures that pointer1 does not break away with the removed node
                    removed_node.nextval = None
                    pointer1 = p1 #places pointer1 on the next node in the list
                    self.decreaselength()
                    continue

                pointer1, pointer2 = self.update_pointers(pointer1, pointer2)

            if self.length == 0: self.empty = True
            return removed_node

        if code == 2:
            pointer1, pointer2 = self.init_pointers()

            index = 0
            indices = []

            while pointer1 is not None:
                if pointer1.dataval == data:
                    #add the "index" of all values matching the removal data parameter
                    indices.append(index)
                index += 1
                pointer1, pointer2 = self.update_pointers(pointer1, pointer2)

            pointer1, pointer2 = self.init_pointers()

            #iterate through the list again to the location of the last matching node
            for _ in range(indices[len(indices) - 1]):
                pointer1, pointer2 = self.update_pointers(pointer1, pointer2)
            
            #remove node here, note that the right-most instance could be the first node in the list
            if pointer1 == self.headval:
                removed_node = self.remove_head()
            elif pointer1 == self.tailval:
                removed_node = self.remove_tail()
            else:
                removed_node = pointer1
                pointer2.nextval = removed_node.nextval
                removed_node.nextval = None
                self.decreaselength()
            
            if self.length == 0: self.empty = True
            return removed_node

    def remove_duplicates(self):
        pointer1 = self.headval.nextval
        pointer2 = self.headval

        while pointer1 is not None:
            if pointer1.dataval == pointer2.dataval:
                data = pointer1.dataval
                pointer1, pointer2 = self.update_pointers(pointer1, pointer2)
                self.remove(data)
                continue
            pointer1, pointer2 = self.update_pointers(pointer1, pointer2)

    def reverselist_inplace(self):
        pass

    def sorted_intersect(self, list2):
        l1 = self.deep_copy()
        l2 = list2.deep_copy()
        
        l1.append_list(l2)
        l1.printlist()
        print()

        l1.insert_sort()
        l1.printlist()
        print()

        l1.remove_duplicates()
        l1.printlist()
        print()

        return l1
            

    def sorted_merge(self, list2):
        self.append_list(list2)
        self.insert_sort()

    def shuffle_merge(self, list2):
        
        i = 0
        while list2.headval is not None:
            if i % 2 == 1:
                self.insert_nth(i, list2.remove_head())
            
            i += 1


if __name__ == '__main__':
    list1 = SLinkedList()
    list2 = SLinkedList()

    for i in range(5):
        list1.append(i)

    for i in range(3,8):
        list2.append(i)

    list3 = list1.sorted_intersect(list2)

    list3.printlist()