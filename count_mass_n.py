def highest_rank(arr):
    result = []
    key = set(arr)
    rez = dict.fromkeys(key, 0)
    for key in arr:
        rez[key] += 1
    max_value = max(rez.values())
    for i in arr:
        if max_value == arr.count(i):
            result.append(i)
    a = (result)
    return max(a)

print(highest_rank(arr=[12, 10, 8, 12, 7, 6, 4, 10, 12, 10]))