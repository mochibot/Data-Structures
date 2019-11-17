class Heap:
    def __init__(self, comparator = None):
        self.storage = []
        self.comparator = comparator

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

    def get_priority(self):
        return self.storage[0]

    def get_size(self):
        return len(self.storage)

    def _bubble_up(self, index):
        if index == 0:
            return

        parent = (index + 1) // 2 - 1
        if self.comparator is None: 
            if self.storage[parent] < self.storage[index]:
                self.storage[parent], self.storage[index] = self.storage[index], self.storage[parent]
        else:
            if self.comparator(self.storage[index], self.storage[parent]):
                self.storage[parent], self.storage[index] = self.storage[index], self.storage[parent]
        
    def _sift_down(self, index):
        left_child = 2 * (index + 1) - 1
        right_child = 2 * (index + 1)

        if left_child > self.get_size() - 1:
            return 

        if self.comparator is None:
            prioritized = left_child if left_child == self.get_size() - 1 or self.storage[left_child] > self.storage[right_child] else right_child

            if self.storage[prioritized] > self.storage[index]:
                self.storage[index], self.storage[prioritized] = self.storage[prioritized], self.storage[index]
        else:
            prioritized = left_child if left_child == self.get_size() - 1 or self.comparator(self.storage[left_child], self.storage[right_child]) else right_child

            if self.comparator(self.storage[prioritized], self.storage[index]):
                self.storage[index], self.storage[prioritized] = self.storage[prioritized], self.storage[index]


''' 
for testing

heap = Heap(lambda x, y: x < y)
heap.insert(6)
heap.insert(7)
heap.insert(5)
heap.insert(10)
heap.insert(8)
heap.insert(1)
heap.insert(2)
heap.insert(5)
print(heap.storage)

descending_order = []

while heap.get_size() > 0:
    descending_order.append(heap.delete())

print(descending_order)
'''