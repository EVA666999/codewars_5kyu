def next_higher(n):
    bit_length = n.bit_length()
    bit = f'{n:0{bit_length}b}'
    count_1_bit = bit.count('1')
    
    # Расширяем диапазон поиска
    for i in range(n + 1, n + n):
        its_bit_length = i.bit_length()
        its_bit = f'{i:0{its_bit_length}b}'
        if its_bit.count('1') == count_1_bit:
            return i

print(next_higher(201326592))
