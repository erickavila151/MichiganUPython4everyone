fname = input("Enter file name: ")
fh = open(fname)
unique_words = []
# Read the file line by line
for line in fh:
# Split the line into individual words
    words = line.split()     
# Append words if they aren't already in our list
    for word in words:
        if word not in unique_words:
             unique_words.append(word)
# Sort the list using Python's standard sort() method
unique_words.sort()
# Print the resulting list
print(unique_words)
