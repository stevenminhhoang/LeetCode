# O(log(n))
def nextGreatestLetter(letters, target):
    left, right = 0, len(letters)
    while left < right:
        mid = left + (right - left) // 2
        if letters[mid] <= target:
            left = mid + 1
        else:
            right = mid

    return letters[left] if letters[left] > target else letters[0]
    # return letters[left] if left <= len(letters) - 1 else letters[0]

print(nextGreatestLetter(["c", "f", "j"], "c"))
