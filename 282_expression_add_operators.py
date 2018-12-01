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
    if not num:
        return []

    backtrack(res, "", num, target, 0, 0, 0)
    return res


print(expression("105", 5))
