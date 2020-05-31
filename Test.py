word = input()
vowels = ['a', 'e', 'i', 'o', 'u']


b = 0
while b == 0:
    for char_num in range(1, len(word)):
        if word[char_num] in vowels:
            indicator = char_num
            b += 1

print(indicator)