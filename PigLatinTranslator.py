def EngToPigLatin(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if word[0] in vowels:
        return word + 'way'

    else:
        length = len(word)
        b = 0
        while b == 0:
            for char_num in range(0, length):
                if word[char_num] in vowels:
                    b += 1
                    break

        first_char_set = word[0:char_num]
        second_char_set = word[char_num:]
        return second_char_set + first_char_set + 'ay'
