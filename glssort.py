def is_alt(s):
    vowels =  ['a', 'e', 'i', 'o', 'u']
    for i in range(len(s)- 1):
        a = s[i] in vowels
        b = s[i + 1] in vowels
        if a == b:
            return False
    return True
        

            
print(is_alt(s='orange'))