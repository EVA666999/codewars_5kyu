def prexf(arr):
    words = arr.split(',')
    max_prefix = words[0]
    for i in range(len(max_prefix)):
        last_simbol = max_prefix[i-1]
        print(last_simbol)
        

print(prexf(arr='flower,flow,flight'))    