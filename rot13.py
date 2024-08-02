def rot13(message):   
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    blabla = ['!','@','#','$','%','^','&','*','(',')','_','+','|','"','}','{','?','>','<','}','.','~',':',';','=','()','-']
    result = []
    for i in range(len(message)):
        for j in range(len(alphabet)):
            if message[i] == alphabet[j]:
                result.append(alphabet[j-13])
            elif message[i].upper() == alphabet[j].upper():
                result.append(alphabet[j-13].upper())
        if message[i].isdigit():
            result.append(message[i])
        elif message[i] in blabla:
            result.append(message[i])
        elif message[i] == ' ':
            result.append(' ')
    return ''.join(result)

print(rot13(message="!@#$%^&*+?~()_-+=:;"))
