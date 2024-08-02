def count_smileys(arr):
    smileface = [':-D', ';-D',':~D', ';~D', ':-)', ':~)', ';-)', ';~)',':)',';)',';D',':D']
    result = []
    for i in arr:
        if i in smileface:
            result.append(i)
    return len(result)

print(count_smileys(arr=[';]', ':[', ';*', ':$', ';-D']))