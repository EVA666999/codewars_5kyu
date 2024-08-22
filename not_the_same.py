def hamming(a,b):
    count = 0
    for i, j in zip(a, b):
        if i != j:
            count += 1
    return count
print(hamming(a='I like turtles', b='I like turkeys'))