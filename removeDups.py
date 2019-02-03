# Remove all duplicates from a string Eg: String: AABGFHHHAB => ABGFHAB'''
myDups = 'AABGFHHHAB1120023GGXMNZAAZ1998'
noDups = []
for char in myDups:
    if char not in noDups:
        noDups.append(char)
newNoDups = ''.join(noDups)
print(newNoDups)
