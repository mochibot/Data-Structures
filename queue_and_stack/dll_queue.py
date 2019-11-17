import sys, os
dir_name = os.getcwd()
sys.path.append(dir_name + '\\doubly_linked_list')    #I had to add this to the path name for the import to work
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()
    
    def __str__(self):
        node = self.storage.head
        while node and node.next:
            print(node.value)
            node = node.next

    def enqueue(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            return
        else:
            self.size -= 1
            return self.storage.remove_from_tail()

    def len(self):
        return self.size
