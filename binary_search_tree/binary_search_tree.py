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
        # my original approach (recursive)
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
        
        # adding iterative approach for fun
        # while self:
        #     if value > self.value:
        #         if not self.right:
        #             self.right = BinarySearchTree(value)
        #             return
        #         self = self.right
        #     else:
        #         if not self.left:
        #             self.left = BinarySearchTree(value)
        #             return
        #         self = self.left
            

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # my original approach (recursive)
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

        # adding iterative approach for fun
        # while self:
        #     if self.value == target:
        #         return True
            
        #     if target > self.value:
        #         if not self.right:
        #             return False
        #         self = self.right
        #     else:
        #         if not self.left:
        #             return False
        #         self = self.left

    # Return the maximum value found in the tree
    def get_max(self):
        # my original approach (iterative)
        if not self.right:
            return self.value

        curr_max = self.value      # I realized later that I dont have to check for max but I was being paranoid
        node = self.right
        while node:
            curr_max = max(node.value, curr_max)
            node = node.right
        return curr_max

        # adding recursive approach for fun
        #    if not self.right:
        #        return self.value
        #    return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # my BFS approach
        # queue = Queue()
        # queue.enqueue(self)
        # while queue.len() > 0:
        #     node = queue.dequeue()
        #     cb(node.value)
        #     if node.left:
        #         queue.enqueue(node.left)
        #     if node.right:
        #         queue.enqueue(node.right)
        
        # my recursive approach
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)


    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node.left:
            self.in_order_print(node.left)
        print(node.value) 
        if node.right:
            self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        queue = Queue()
        queue.enqueue(self)
        while queue.len() > 0:
            node = queue.dequeue()
            print(node.value)
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        stack = Stack()
        stack.push(self)
        while stack.len() > 0:
            node = stack.pop()
            print(node.value)
            if node.left:
                stack.push(node.left)
            if node.right:
                stack.push(node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT (top to bottom, left to right)
    def pre_order_dft(self, node):
        if not node.left or not node.right:
            print(node.value)  
        if node.left and node.right:
            print(node.value)
        if node.left:
            self.pre_order_dft(node.left)
        if node.right:
            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT (bottom to top, left to right)
    def post_order_dft(self, node):
        if not node.left and not node.right:
            print(node.value)  
        if node.left:
            self.post_order_dft(node.left)
        if node.right:
            self.post_order_dft(node.right)
        if node.left or node.right:
            print(node.value)


'''for testing 
tree = BinarySearchTree(1)
tree.insert(8)
tree.insert(5)
tree.insert(7)
tree.insert(6)
tree.insert(3)
tree.insert(4)
tree.insert(2)

def print_self(n):
    print(n)

tree.for_each(print_self)
tree.in_order_print(tree)
tree.bft_print(tree)
tree.dft_print(tree)
tree.pre_order_dft(tree)
tree.post_order_dft(tree)
'''