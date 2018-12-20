def convertToTitle(n):
   # if n == 0:
   #    return ""
   # else:
   #    return convertToTitle((n - 1) // 26) + chr((n - 1) % 26 + ord('A'))
   return ord('A')

print(convertToTitle(3))

def excel_title(n):
    res = []
    while n:
        res.append(chr((n - 1) % 26 + ord("A")))
        n = (n - 1) // 26

    return "".join(res[::-1])

print(excel_title(701))
