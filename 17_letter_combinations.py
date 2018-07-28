# O(4^n)
def letter_combinations(digits):
    def backtrack(lis, digits, temp, start, dic):
        if start == len(digits):
            lis.append("".join(temp[:]))
        else:
            for char in dic[digits[start]]:
                temp.append(char)
                backtrack(lis, digits, temp, start + 1, dic)
                temp.pop()


    dic = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
            }
    if not digits:
        return []

    lis = []
    backtrack(lis, digits, [], 0, dic)
    return lis

print(letter_combinations("234"))
