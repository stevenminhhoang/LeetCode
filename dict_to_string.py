map = {"a": "apple", "b": {"b": "blueberry", "c": "cranberry"}}
dic = {"a": "apple", "b": "blueberry", "c": "cranberry"}
# string = "a:apple,b:blueberry,c:cranberry"

def dict_to_string(dic):
    if len(dic.keys()) == 0:
        return ""
    res = ""
    res += "{"
    for key in dic:
        res += key + ":"
        if isinstance(dic[key], dict):
            res += dict_to_string(dic[key])
        else:
            res += dic[key]

        res += ","

    res = res[:len(res) - 1] + "}"
    return res


string = dict_to_string(map)[1:-1]
string2 = dict_to_string(dic)[1:-1]
# print(string2)

def string_to_dict(string):
    stack = []
    i = 0
    start = 0
    dic = {}
    while i < len(string):
        if string[i] == ':':
            key = string[start:i]
            stack.append(key)
            start = i + 1
        elif string[i] == ',':
            val = string[start:i]
            dic[stack.pop()] = val
            start = i + 1
        elif string[i] == '{':
            end = i + 1
            while end < len(string) and string[end] != '}':
                end += 1

            curr_string = string[i + 1:end]
            print(curr_string)
            map = string_to_dict(curr_string)
            # dic[stack.pop()] = map
            print(map)



        i += 1

    if stack:
        dic[stack.pop()] = val

    return dic

print(string_to_dict(string))



# string_to_dict(string[1:len(string)-1])
