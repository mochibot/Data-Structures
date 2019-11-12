import sys, os
dir_name = os.getcwd()
sys.path.append(dir_name + '\\doubly_linked_list')   #I had to add this to the path name for the import to work
from doubly_linked_list import DoublyLinkedList


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.nodes = 0
        self.entries = DoublyLinkedList()
        self.storage = {}

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):     
        if key in self.storage.keys():
            node = self.storage[key]
            self.entries.move_to_front(node)
            return node.value
        else:
            return None

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if self.nodes == self.limit:                # if limit is reached
            if key in self.storage:                 # overwrite existing key:value pair
                self.entries.move_to_front(self.storage[key])
                self.storage[key].value = value
            else:                                   # if new key does not exist in cache
                least = self.entries.tail           # remove least used entry and add new key:value pair
                self.entries.remove_from_tail() 
                self.storage = {k:v for k,v in self.storage.items() if v != least}
                self.entries.add_to_head(value)
                self.storage[key] = self.entries.head
        else:                                       
            self.entries.add_to_head(value)
            self.nodes += 1
            self.storage[key] = self.entries.head