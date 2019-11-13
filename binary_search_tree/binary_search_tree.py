import sys, os
dir_name = os.getcwd()
sys.path.append(dir_name + '\\queue_and_stack') 
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        node = BinarySearchTree(value)
        if value > self.value:
            if not self.right: 
                self.right = node
                return
            return self.right.insert(value)
        else:
            if not self.left: 
                self.left = node
                return
            return self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        
        if target > self.value:
            if not self.right:
                return False
            if self.right.value == target:
                return True
            return self.right.contains(target)
        else:
            if not self.left:
                return False
            if self.left.value == target:
                return True
            return self.left.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if not self.right:
            return self.value

        curr_max = self.value
        node = self.right
        while node:
            curr_max = max(node.value, curr_max)
            node = node.right
        return curr_max

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # BFS approach
        # queue = Queue()
        # queue.enqueue(self)
        # while queue.len() > 0:
        #     node = queue.dequeue()
        #     cb(node.value)
        #     if node.left:
        #         queue.enqueue(node.left)
        #     if node.right:
        #         queue.enqueue(node.right)
        
        #recursive approach
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)
        if not self.left or not self.right:
            return


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass


''' for testing
tree = BinarySearchTree(5)
tree.insert(2)
tree.insert(3)
tree.insert(7)
tree.insert(6)

def print_self(n):
    print(n)

tree.for_each(print_self)
'''