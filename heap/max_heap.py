'''
Heap
- Special case of balanced binary tree data structure (each level is completed filled, except for the bottommost, filled left to right)
- The root node key is compared with its children and arranged accordingly (value of parent >= value of child)
- Can be implemented with linked list or array (easier as array)
- Number the nodes in the heap from top to bottom, left to right, and store the value in the corresponding index in array
- Given the index (i) of a node, the index of parent (i/2), left child (2i), right child (2i + 1) can be computed

'''

class Heap:
    def __init__(self):
        self.storage = []

    def insert(self, value):
        self.storage.append(value)
        index = self.get_size() - 1

        while index >= 0:
            self._bubble_up(index)
            index = (index + 1) // 2 - 1

    def delete(self):
        top = self.storage.pop(0)
        size = self.get_size()

        index = 0
        while index <= size:
            self._sift_down(index)
            index = 2 * (index + 1) - 1
        return top

    def get_max(self):
        if len(self.storage) > 0:
            return self.storage[0]
        else:
            return None

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        if index == 0:
            return

        parent = (index + 1) // 2 - 1
        if self.storage[parent] < self.storage[index]:
            self.storage[parent], self.storage[index] = self.storage[index], self.storage[parent]

    def _sift_down(self, index):
        left_child = 2 * (index + 1) - 1
        right_child = 2 * (index + 1)

        if right_child > self.get_size() - 1:
            return 

        bigger = left_child if self.storage[left_child] > self.storage[right_child] else right_child
        if self.storage[bigger] > self.storage[index]:
            self.storage[index], self.storage[bigger] = self.storage[bigger], self.storage[index]


''' 
for testing 

heap = Heap()
heap.insert(6)
heap.insert(7)
heap.insert(5)
heap.insert(8)
heap.insert(10)
heap.insert(1)
heap.insert(2)
heap.insert(5)
print(heap.storage)

descending_order = []

while heap.get_size() > 0:
    descending_order.append(heap.delete())

print(descending_order)
'''