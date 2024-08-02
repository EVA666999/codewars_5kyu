def find_uniq(arr):
    count_dict = {}
    for n in arr:
        if n in count_dict:
            count_dict[n] += 1
        else:
            count_dict[n] = 1

    for n in arr:
        if count_dict[n] == 1:
            return n

print(find_uniq([3, 10, 3, 3, 3]))
