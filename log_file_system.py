import collections
def path(arr):
    dic = collections.defaultdict(set)
    for path in arr:
        subdir = path.split("/")
        for i in range(len(subdir) - 1):
            dic[subdir[i]].add(subdir[i + 1])
        dic[subdir[-1]] = {}

    print(dic)





arr = ["dir/subdir1/subdir2", "dir/subdir1/subdir3", "root/subdir4"]
print(path(arr))
