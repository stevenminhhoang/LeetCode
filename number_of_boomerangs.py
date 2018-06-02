def number_of_boomerangs(points):
    res = 0
    for p1 in points:
        cmap = {}
        for p2 in points:
            d = distance(p1, p2)
            cmap[d] = cmap.get(d, 0) + 1
        for k in cmap:
            res += cmap[k] * (cmap[k] - 1)

    return res

def distance(x, y):
    return (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2


print(number_of_boomerangs([[0,0],[1,0],[2,0]]))
