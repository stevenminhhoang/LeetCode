def detect_capital_use(word):
    return word.isupper() or word.islower() or word.istitle()

print(detect_capital_use("FLaG"))
