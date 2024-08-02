def get_sum(a,b):
    result = []
    if a < b:
        for i in range(a,b+1):
            result.append(i)
        return sum(result)
    else:
        for i in range(b,a+1):
            result.append(i)
        return sum(result)
print(get_sum(a=-1, b=2))