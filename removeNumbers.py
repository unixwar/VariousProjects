# Remove numbers from a string:
unwantedDigits = '1234567890'
myString = "ALPH99Ad786 FL22202 123450MTY vT100 WA98052"
print(myString)
for character in unwantedDigits:
    myString = myString.replace(character, '')
print(myString)
