line = 'From stephen.marquad@uct.ac.za Sat Jan 5 09:14:16 2008'
#it gets divided in 3
words = line.split()    
email = words[1]
pieces = email.split('@')
print(pieces[1])

