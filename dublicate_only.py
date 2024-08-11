def only_duplicates(st):
    result = []
    for i in st:
        if st.count(i) >= 2:
            result.append(i)
    return ''.join(result)

print(only_duplicates(st='abccdefee'))