# O(n * 2^n)
def restore_IP_addresses(s):
    def dfs(lis, path, start, s):
        if start == 4:
            if not s:
                lis.append(path[:-1])
            return # backtracking
        for i in range(1, 4):
            # the digits we choose should no more than the length of s
            if i <= len(s):
                #choose one digit
                if i == 1:
                    dfs(lis, path + s[:i] + '.', start + 1, s[i:])
                #choose two digits, the first one should not be "0"
                elif i == 2 and s[0] != "0":
                    dfs(lis, path + s[:i] + '.', start + 1, s[i:])
                #choose three digits, the first one should not be "0", and should less than 256
                elif i == 3 and s[0] != "0" and int(s[:3]) <= 255:
                    dfs(lis, path + s[:i] + '.', start + 1, s[i:])

    lis = []
    dfs(lis, "", 0, s)
    return lis


print(restore_IP_addresses("25525511135"))

# Ad hoc
def restore_IP_addresses(s):
    ans = []
    for a in range(1, 4):
        for b in range(1, 4):
            for c in range(1, 4):
                for d in range(1, 4):
                    if a + b + c + d == len(s):
                        A = int(s[0:a])
                        B = int(s[a:a+b])
                        C = int(s[a+b:a+b+c])
                        D = int(s[a+b+c:a+b+c+d])
                        if A <= 255 and B <= 255 and C <= 255 and D <= 255:
                            temp = "{}.{}.{}.{}".format(A,B,C,D)
                            if len(temp) == len(s) + 3:
                                ans.append(temp)

    return ans

# print(restore_IP_addresses("25525511135"))
