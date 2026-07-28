#spaces do not matter to split, so you can put a bunch of them
line = 'A lot                        of spaces'
etc = line.split()
print(etc)

#delimiter for below

line = 'first;second;third'
thing = line.split()
print(len(thing))

#You can specify what delimiter character to use in the splitting

thing = line.split(';')
print(thing)
print(len(thing))