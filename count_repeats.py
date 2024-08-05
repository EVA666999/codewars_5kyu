def count_repeats(txt):
    count = 0
    for i in range(len(txt) -1):
        if txt[i] and txt[i+1] == txt[i]:
            count += 1
    return count

print(count_repeats(txt='ab cca'))