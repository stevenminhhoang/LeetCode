# O(n)
def circularArrayLoop(nums):
    def get_index(i):
        n = len(nums)
        return (i + nums[i] + n) % n

    for i in range(len(nums)):
        if nums[i] == 0:
            continue

        j = i
        k = get_index(i)
        while nums[k] * nums[i] > 0 and nums[get_index(k)] * nums[i] > 0:
            if j == k:
                if j == get_index(j):
                    break
                return True

            j = get_index(j)
            k = get_index(get_index(k))

        j = i
        while nums[j] * nums[i] > 0:
            next = get_index(j)
            nums[j] = 0
            j = next

    return False

print(circularArrayLoop([2, -1, 1, 2, 2]))
