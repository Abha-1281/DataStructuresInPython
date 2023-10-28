# Program to insert an element in a heap

class Heap:
    def __init__(self):
        self.heap = []

    def _parent_(self, i):
        return (i - 1) // 2

    def _left_child(self, i):
        return 2 * i + 1

    def _right_child(self, i):
        return 2 * i + 2

    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, data):
        self.heap.append(data)
        curr = len(self.heap) - 1  # index of the current element which is just now inserted
        self.heapify(curr)  # call heapify on the inserted element to move this element to its correct place

    def heapify(self, curr):
        if curr > 0:   # no need to call heapify for the parent element
            if self.heap[self._parent_(curr)] < self.heap[curr]:
                self.swap(curr, self._parent_(curr))
                curr = self._parent_(curr)
                self.heapify(curr)


if __name__ == '__main__':
    maxheap = Heap()
    maxheap.insert(10)
    maxheap.insert(5)
    maxheap.insert(3)
    maxheap.insert(2)
    maxheap.insert(4)
    maxheap.insert(15)
    print(maxheap.heap)
