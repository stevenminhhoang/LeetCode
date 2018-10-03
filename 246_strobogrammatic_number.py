def isStrobogrammatic(num):
    dic = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
    left, right = 0, len(num) - 1
    while left <= right:
        if num[left] not in dic or num[right] not in dic:
            return False
        if dic[num[left]] != num[right]:
            return False
        left += 1
        right -= 1

    return True

print(isStrobogrammatic("69"))
