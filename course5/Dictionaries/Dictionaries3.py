#USING A FOR AND ALSO THE IN IN OUR DICTIONARIES
#when we encounter a new name we need to add a new entry in the dictionary and if this the second or later time we have seen the name, we simply add one to the count in the dictionary under that 


#IT CAPTURES THE MOMENT WHEN WE FIRST ENCOUNTER A NAME, AND ALSO CAPTURES THE MOMENT WHEN WE ARE ADDING ONE TO IT

counts = dict()

names = ['Juan', 'Erick', 'Brayan', 'Michelle', 'Dayra', 'Irving', 'Dayra', 'Erick']

for name in names :
    if name not in counts :
        counts[name] = 1
    else :
        counts [name] = counts [name] + 1
print(counts)