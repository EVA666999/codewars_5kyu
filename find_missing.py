def find_missing(sequence):
    d1 = sequence[1] - sequence[0]
    d2 = sequence[2] - sequence[1]
    real_d = d1 if d1 == d2 else d2
    for i in range(1,len(sequence)):
        if sequence[i] - sequence[i-1] != real_d:
            return sequence[i-1] + real_d


print(find_missing(sequence=[4, 8, 12, 16, 20, 24, 28, 32, 40]))