class Heap:
    def __init__(self, heap_arr):
        self.heap_arr = heap_arr

    def pop_max_element(self):
        max_ele = self.heap_arr[0]
        self.heap_arr[0], self.heap_arr[len(heap_arr) - 1] = self.heap_arr[len(heap_arr) - 1], self.heap_arr[0]
        self.heap_arr.pop()
        self.prune_down(0)
        return max_ele
    
    def prune_down(self, idx):
        if 2 * idx + 1 > len(self.heap_arr) - 1:
            return

        left = 2 * idx + 1
        right = 2 * idx + 2
        max_idx = idx

        if left <= len(self.heap_arr) - 1 and self.heap_arr[max_idx] < self.heap_arr[left]:
            max_idx = left

        if right <= len(self.heap_arr) - 1 and self.heap_arr[max_idx] < self.heap_arr[right]:
            max_idx = right

        if max_idx != idx:
            self.heap_arr[max_idx], self.heap_arr[idx] = self.heap_arr[idx], self.heap_arr[max_idx]
            self.prune_down(max_idx)
    
    def build_heap(self):
        idx = len(self.heap_arr) - 1
        while idx >= 0:
            self.prune_down(idx)
            idx -= 1
        print("the heap build is ", self.heap_arr)

    def heap_sort(self):
        for i in range(len(self.heap_arr)):
            print(self.pop_max_element())


if __name__ == '__main__':
    heap_arr = [55, 33, 11, 22, 33, 77, 88, 100]
    heap = Heap(heap_arr)
    heap.build_heap()
    heap.heap_sort()
