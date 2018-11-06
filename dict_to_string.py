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
print(string2)

def string_to_dict(string):
    stack = []
    i = 0
    start = 0
    while i < len(string):
        if string[i] == ':':
            key = string[start:i]
            stack.append(key)


        i += 1





# string_to_dict(string[1:len(string)-1])
