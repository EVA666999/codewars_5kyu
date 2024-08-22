def dig_pow(n, p):
    result = []
    for i in str(n):
        i = int(i)**p
        p +=1
        result.append(i)
    k = sum(result)
    resalt = 0
    for r in range(10000):
        if n * r == k:
            resalt += r
    if resalt != 0:
        return resalt
    else:
        return -1

print(dig_pow(n=46288, p=3))