# O(n * sqrt(n))
import collections
def perfect_squares(n):
    squares = [i * i for i in range(1, n + 1) if i * i <= n]
    visited = set()
    count = 0
    queue = collections.deque()
    queue.append(n)

    while queue:
        count += 1
        size = len(queue)
        for i in range(size):
            curr = queue.popleft()
            for num in squares:
                new_val = curr - num
                if new_val < 0:
                    break
                if new_val == 0:
                    return count
                if new_val not in visited:
                    visited.add(new_val)
                    queue.append(new_val)

    return -1

print(perfect_squares(1))
