from collections import Counter

def can_construct(ransomNote, magazine):
      a = Counter(ransomNote)
      b = Counter(magazine)
      return not a - b

print(can_construct("aa","aab"))
