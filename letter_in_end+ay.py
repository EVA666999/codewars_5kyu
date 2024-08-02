def pig_it(text):
    words = text.split()
    reversed_words = [word[1:]+word[0] for word in words]
    result = []
    for i in reversed_words:
        if i.isalpha():
            i += 'ay'
            result.append(i)
        else:
            result.append(i)
    return ' '.join(result)
    
print(pig_it('Hello world ?'))