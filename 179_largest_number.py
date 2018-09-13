# O(n * log(n))
class LargerNumKey(str):
    def __lt__(x, y):
        return x + y > y + x


def largest_number(nums):
    nums_string = sorted(map(str, nums), key = LargerNumKey)
    if nums_string[0] == 0:
        return "0"

    return "".join(nums_string)


print(largest_number([10, 2]))
print(largest_number([3,30,34,5,9]))
