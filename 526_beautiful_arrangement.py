# O(k) k is number of valid permutations
# def beautiful_arrangement(N):
#     def backtrack(nums, start):
#         global count
#         if start == len(nums):
#             count += 1
#         else:
#             for i in range(start, len(nums)):
#                 nums[i], nums[start] = nums[start], nums[i]
#                 if nums[start] % (start + 1) == 0 or (start + 1) % nums[start] == 0:
#                     backtrack(nums, start + 1)
#                 nums[i], nums[start] = nums[start], nums[i]
#
#
#
#     global count
#     count = 0
#     nums = range(1, N + 1)
#     backtrack(nums, 0)
#     return count
#
# print(beautiful_arrangement(2))

# Backtracking
def beautiful_arrangement(N):
    def backtrack(N, start, visited):
        global count
        if start > N:
            count += 1
        else:
            for i in range(1, N + 1):
                if visited[i] == False and (start % i == 0 or i % start == 0):
                    visited[i] = True
                    backtrack(N, start + 1, visited)
                    visited[i] = False



    global count
    count = 0
    visited = [False for i in range(N + 1)]
    backtrack(N, 1, visited)
    return count

print(beautiful_arrangement(2))
