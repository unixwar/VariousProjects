# Removing unwanted characters from a string. In this case removing digits from a string. (example 1)

myString = "ALPH99Ad786 FL22202 123450MTY vT100 WA98052"
digits = '0123456789'
newString = []

for char in myString:
    if char not in digits:
        newString.append(char)
newLetters = ''.join(newString)
print(newLetters)
