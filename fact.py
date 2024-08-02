def zeros(n):
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count
        

    
print(zeros(n=1000000000))