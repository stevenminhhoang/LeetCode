# def plus_one(digits):
#     i = len(digits) - 1
#
#     while i >= 0:
#         if digits[i] == 9:
#             digits[i] = 0
#             i -= 1
#         else:
#             digits[i] += 1
#             return digits
#
#     return [1] + digits


def plus_one(digits):
    digits[-1] += 1
    for i in reversed(range(1, len(digits))):
        if digits[i] != 10:
            break
        else:
            digits[i] = 0
            digits[i-1] += 1

    if digits[0] == 10:
        digits[0] = 0
        return [1] + digits

    return digits



print(plus_one([9,9]))
