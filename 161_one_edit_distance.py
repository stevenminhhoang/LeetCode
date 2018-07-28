# O(n)
def one_edit_distance(s, t):
    def edit_replace(a, b):
        found_diff = False
        for i in range(len(a)):
            if a[i] != b[i]:
                if found_diff == True:
                    return False
                found_diff = True
        return found_diff

    def edit_insert(a, b):
        i, j = 0, 0
        while i < len(a) and j < len(b):
            if a[i] != b[j]:
                if i != j:
                    return False
                i += 1
            else:
                i += 1
                j += 1

        return True

    if not s and not t:
        return False
    if len(s) == len(t):
        return edit_replace(s, t)
    elif len(s) - len(t) == 1:
        return edit_insert(s, t)
    elif len(t) - len(s) == 1:
        return edit_insert(t, s)
    else:
        return False

print(one_edit_distance("1213", "1213"))
