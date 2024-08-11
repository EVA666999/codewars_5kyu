def narcissistic(value):
    result = []
    for i in str(value):
        result.append(int(i)**len(str(value)))
    return sum(result) == value
        

print(narcissistic(value=122))