def print_json(s):
    res = []
    i = 0
    k = 0
    while i < len(s):
        if s[i] == ' ':
            i += 1
        elif s[i] in ('{', '['):
            res.append('\t' * k + s[i])
            k += 1
            i += 1
        elif s[i] in ('}', ']'):
            k -= 1
            res.append('\t' * k + s[i])
            i += 1
        elif s[i] == ',':
            res[-1] += ','
            i += 1
        else:
            start = i
            while i < len(s) and s[i] not in ('{', '}', '[', ']', ','):
                i += 1
            curr_string = s[start:i]
            res.append('\t' * k + curr_string)

    for x in res:
        print(x)





dict = {"id": "0001", "type": "donut", "name": "Cake", "ppu": 0.55, "batters":{"batter":[{ "id": "1001", "type": "Regular" },{ "id": "1002", "type": "Chocolate" }]},"topping":[{ "id": "5001", "type": "None" },{ "id": "5002", "type": "Glazed" }]}
string = str(dict)
print_json(string)
