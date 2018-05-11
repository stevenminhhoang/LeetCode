def self_dividing_numbers(left, right):
    ans = []
    for num in range(left, right + 1):
        if self_dividing_number(num):
            ans.append(num)
        else:
            continue
    return ans

def self_dividing_number(n):
    x = n
    while x > 0:
        digit = x % 10
        x = x // 10
        if digit == 0 or n % digit != 0:
            return False
    return True


self_dividing_numbers(1, 22)
