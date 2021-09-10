def get_occurrences_dict(s):
    d = dict()
    for char in s.lower():
        if char not in d:
            d[char] = 1
        else:
            d[char] += 1
    return d
