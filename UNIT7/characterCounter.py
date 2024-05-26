def countCharacters(s):
    counts = dict() # Create an empty dictionary alt way: counts = {}
    for c in s: # For each character in the string
        if c in counts: # If the character is already in the dictionary
            counts[c] += 1 # Increment the count
        else:
            counts[c] = 1
    return counts
name = input('Enter a name: ')
print(countCharacters(name))