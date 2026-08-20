#The get Method for Dictionaries

#the pattern of checking to see if a key is already in a dictionary and assuming a default value if the key is not there is so common that there is a method called GET() that does this for us

counts = dict()

names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']

#these four line of code, will be replaced by only 1 line below
# for name in names :
#     if name in counts:
#         x = counts [name]
#     else :
#         x = 0

#2 parameters, x will become name or 0, it depends
for name in names :
    counts[name] = counts.get(name, 0) + 1
    print(counts)


