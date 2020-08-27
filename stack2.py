# your code goes here



	
def heapify(idx, heap):
	if 2 * idx + 1 >= len(heap):
		return
	
	left = 2 * idx + 1
	right = 2 * idx + 2
	
	max_idx = idx
	
	if left < len(heap) and heap[left] > heap[max_idx]:
		max_idx = left
	
	if right < len(heap) and heap[right] > heap[max_idx]:
		max_idx = right
		
	if max_idx != idx:
		heap[max_idx], heap[idx] = heap[idx], heap[max_idx]
		heapify(max_idx, heap)
		
def get_max(heap):
	max_ele = heap[0]
	heap[0], heap[len(heap) - 1] = heap[len(heap) - 1], heap[0]
	heap = heap[:-1]
	heapify(0)
	return max_ele
	
def build(heap):
	idx = len(heap) - 1
	while idx >= 0:
		heapify(idx, heap)
		idx -= 1
		
if __name__ == '__main__':
	heap = [1,55,33,11,223,42,12]
	build(heap)
	
	n = len(heap)
	for i in range(n):
		print(get_max(heap))

