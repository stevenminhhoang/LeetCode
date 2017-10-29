def check_record(s):
    if s.count("A") > 1:
        return False
    return "LL" in s
