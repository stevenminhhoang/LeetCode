# O(log(m) + log(n)) = O(log(mn))
def searchMatrix(matrix, target):
    if not matrix or target is None:
        return False

    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1
    while left <= right:
        mid = left + (right - left) // 2
        num = matrix[mid // cols][mid % cols]
        if num == target:
            return True
        elif num < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]

print(searchMatrix(matrix, 11))
