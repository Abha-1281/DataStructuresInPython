# Program to sort an array using heap sort.

# The solution is to first build a max heap from the given array by using sinkDown Heapify method for all the
# internal nodes from n//2 -1 to 0

# once the max heap is build, swap each element with the root node and then call sinkDown heapify for the root node


def sinkDown(curr, n, arr):
    largest = curr
    left = 2 * curr + 1
    right = 2 * curr + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right

    if curr != largest:
        arr[curr], arr[largest] = arr[largest], arr[curr]
        sinkDown(largest, n, arr)


def heapSort(arr, n):
    
    # first build the max heap

    for i in range(n // 2 - 1, 0, -1):
        sinkDown(i, n, arr)

    # swap the root and the last node and call the sink Down heapify on the root node with reduced arr length since
    # we don't want to consider heapify on the last element as its now sorted

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        sinkDown(0, i, arr)


if __name__ == '__main__':
    arr = [12, 11, 13, 5, 6, 7]
    heapSort(arr, len(arr))
    print(arr)
