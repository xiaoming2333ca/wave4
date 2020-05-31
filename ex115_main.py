import pig_latin_translator
line = str(input("Please Enter a Sentence >"))

x = line.split(" ")
length = len(x)
output = []

for num in range(0, length):
    print(pig_latin_translator.EngToPigLatin(x[num]), end=" ")
