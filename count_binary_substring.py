def count_binary_substring(s):
   count = 0
   zeros = 0
   ones = 0
   for i in range(len(s)-1):
       for j in range(i+1,len(s)):
