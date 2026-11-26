#USING re.search() Like find()

import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()  
    if re.search('From:', line):  #Library name + function
        print(line)

# hand = open('mbox-short.txt')
# for line in hand:
#     line = line.rstrip()
#     if line.find('From:') >= 0:
#         print(line)


#Using re.search() Like startswith()

