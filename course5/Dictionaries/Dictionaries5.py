#How to count a list of words, and also find the most common word in it

counts = dict()
print('Enter a line of text: ')
line = input('')

words = line.split()

print('Words:', words)

print ('Counting... ')

for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts', counts)

