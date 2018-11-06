import collections
def range_addition(length, updates):
    arr = [0] * length
    count = collections.Counter()
    for update in updates:
        start, end, inc = update[0], update[1], update[2]
        

    for key, val in count.items():
        arr[key] = val

    return arr

print(range_addition(5, [[1,3,2],[2,4,3],[0,2,-2]]))
