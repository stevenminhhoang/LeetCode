def read_binary_watch(n):
    def dfs(n, hours, mins, index):
        if hours > 11 or mins > 59:
            return
        if not n:
            res.append(str(hours) + ":" + "0"*(mins < 10) + str(mins))
            return

        for i in range()

    res = []
