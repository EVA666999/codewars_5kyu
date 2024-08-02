def first_non_repeating_letter(s):
    if s == '' or s is None:
        return ''
    s_lower = s.lower()
    for index, item in enumerate(s_lower):
        if s_lower.count(item) == 1:
            return s[index]
    return ''
print(first_non_repeating_letter(s='sTreSS'))


 