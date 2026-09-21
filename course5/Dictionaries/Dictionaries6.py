#DEFNITE LOOPS AND DICTIONARIES

#even though dictionaries are not stored in order, we can write a for loop that goes through all the entries in a dictionary - actually it goes through all of the keys in the dictionary and looks up the values

counts = { 'Chuck': 1, 'fred' : 42, 'jan': 100}
for key in counts:
    print(key, counts[key])