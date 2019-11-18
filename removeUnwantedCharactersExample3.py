# Removing unwanted characters from a string. In this case appending non-digit character to list. (example 3)

myString = "ALPH99Ad786 FL22202 123450MTY vT100 WA98052"
digits = '0123456789'
newString = []

for char in myString:
    if char in digits:
        continue
    else:
        newString.append(char)
print(''.join(newString))

