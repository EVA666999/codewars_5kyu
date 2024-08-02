def alphanumeric(password):
    abv = "!@.#$=%^&*()_+}{|:?><~'\" `[,-]/');" + ''.join(chr(i) for i in range(32))
    for i in abv:
        for j in password:
            if i in password:
                return False
    if password.isalpha() or password.isnumeric():
        return True
    has_num = False
    has_letter = False
    for i in password:
        if i.isnumeric():
            has_num = True
        if i.isalpha():
            has_letter = True
    if has_num and has_letter:
        return True
    else:
        return False
print(alphanumeric(password='QanaPMwXoK3'))