import PigLatinTranslator
line = str(input("Please Enter a Sentence >"))

x = line.split(" ")
length = len(x)
output = []

for num in range(0, length):
    print(PigLatinTranslator.EngToPigLatin(x[num]), end=" ")
