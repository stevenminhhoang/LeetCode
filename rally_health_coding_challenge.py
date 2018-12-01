from sys import stdin
def expression(num, target):
    def backtrack(res, temp, num, target, index, val, prev_val):
        if index == len(num):
            if val == target:
                res.append(temp)
                return
        for i in range(index, len(num)):
            if index != i and num[index] == "0":
                break
            curr_val = int(num[index: i + 1])
            if index == 0:
                backtrack(res, temp + str(curr_val), num, target, i + 1, curr_val, curr_val)
            else:
                backtrack(res, temp + "+" + str(curr_val), num, target, i + 1, val + curr_val, curr_val)
                backtrack(res, temp + "-" + str(curr_val), num, target, i + 1, val - curr_val, -curr_val)
                backtrack(res, temp + "*" + str(curr_val), num, target, i + 1, val - prev_val + prev_val * curr_val, prev_val * curr_val)

    res = []
    backtrack(res, "", num, target, 0, 0, 0)
    if len(res) == 0:
        print("impossible")
    else:
        for exp in res:
            print(exp)

    print()

N = int(input())
inputs = []
while True:
    try:
        line = input()
    except EOFError:
        break
    inputs.append(line)

for num in inputs:
    expression(num, N)
