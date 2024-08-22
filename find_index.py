def find_index(x, y):
    result  = []
    for i in range(len(x) -1):
        if x[i] + x[i+1] == y:
            result.extend([i, i + 1])
            break
    print(result)

print(find_index(x=[2,7,11,15], y=9))