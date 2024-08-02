def digitwise_addition(N, K):
    my_list = str(N)
    result = []
    for i in my_list:
        i = int(i) + K
        result.append(i)
    return result

print(digitwise_addition(N=9899, K=3))