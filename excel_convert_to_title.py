def convertToTitle(n):
   # if n == 0:
   #    return ""
   # else:
   #    return convertToTitle((n - 1) // 26) + chr((n - 1) % 26 + ord('A'))
   return ord('A')

print(convertToTitle(3))
