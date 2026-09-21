filename = input('Enter file name: ')
if len(filename) < 1 : filename = 'mbox-short.txt'
fh = open(filename)

count = 0

for line in fh:
    wds = line.split()
    if len(wds) < 2 : continue
    if wds[0] != "From" : continue
    print(wds[1])
    count = count + 1

print("There were", count, 'lines in the file with From as the first word')