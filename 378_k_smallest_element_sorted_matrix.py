# Priority Queue
# O(k*log(n))
import heapq

def k_smallest_sorted_matrix(matrix, k):
    heap = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            heapq.heappush(heap, -matrix[i][j])

    while len(heap) > k:
        heapq.heappop(heap)

    return -heap[0]

# Binary Search
# def k_smallest_sorted_matrix(matrix, k):
#     left, right = matrix[0][0], matrix[-1][-1]
#     while left < right:







matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]

print(k_smallest_sorted_matrix(matrix, 8))
