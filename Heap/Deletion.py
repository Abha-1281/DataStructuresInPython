# Program to delete an element from a heap. The deletion operation on Heap deletes the element present at the
# root node of the Heap. Max heap deletes the maximum element whereas minheap deletes a minimum element in a heap


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

    def delete(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            self.heap.pop()
            return

        self.heap[0] = self.heap.pop()  # pop from end and copy it to the root element
        self._sink_down(0)  # call heapify(sinkDown) on the root element to move it to its correct position

    def _sink_down(self, curr):  #find the largest among the left, right, parent and then swap if root is not the largest
        largest = curr
        left = self._left_child(curr)
        right = self._right_child(curr)

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left

        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if curr != largest:  # swap if root is not the largest element
            self.swap(curr, largest)
            self._sink_down(largest)


    def insert(self, data):
        self.heap.append(data)
        curr = len(self.heap) - 1  # index of the current element which is just now inserted
        self._sink_up(curr)  # call heapify(sinkUp) on the inserted element to move this element to its correct place

    def _sink_up(self, curr):
        if curr > 0:  # no need to call heapify for the parent element
            if self.heap[self._parent_(curr)] < self.heap[curr]:
                self.swap(curr, self._parent_(curr))
                curr = self._parent_(curr)
                self._sink_up(curr)


if __name__ == '__main__':
    maxheap = Heap()
    maxheap.insert(10)
    maxheap.insert(5)
    maxheap.insert(3)
    maxheap.insert(2)
    maxheap.insert(4)
    maxheap.insert(15)
    print(maxheap.heap)

    maxheap.delete()
    print(maxheap.heap)
