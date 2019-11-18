# Removing unwanted characters from a string. In this case removing digits from a string. (example 2)

myString = "ALPH99Ad786 FL22202 123450MTY vT100 WA98052"
digits = '0123456789'
newString = []

for char in digits:
    if char in myString:
        myString = myString.replace(char, '')
print(myString)
