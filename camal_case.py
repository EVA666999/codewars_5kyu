def solution(s):
    result = []
    for i in s:
        if i.isupper():
            result += ' '
        result += i
    return ''.join(result)

print(solution(s='camelCasing'))