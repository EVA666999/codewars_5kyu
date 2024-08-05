def alphabet_position(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = []
    for char in text.lower():
        if char in alphabet:
            result.append(str(alphabet.index(char) + 1))
    return ' '.join(result)

print(alphabet_position(text="The sunset sets at twelve o' clock."))