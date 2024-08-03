def digital_root(n):
    result = [int(digit) for digit in str(n)]
    
    sum_result = sum(result)
    
    while sum_result >= 10:
        result = [int(digit) for digit in str(sum_result)]
        sum_result = sum(result)
    
    return sum_result

print(digital_root(n=493193))