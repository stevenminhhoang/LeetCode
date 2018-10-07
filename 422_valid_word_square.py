# O(m * n)
def valid_word_square(words):
    for row in range(len(words)):
        for col in range(len(words[row])):
            if col >= len(words) or row >= len(words[col]) or words[row][col] != words[col][row]:
                return False

    return True

print(valid_word_square([
  "abcd",
  "bnrt",
  "crm",
  "dt"
]))
