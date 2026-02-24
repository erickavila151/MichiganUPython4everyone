fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("Incorrect file name")

for line in fh:
    #rstrip gets rid of the newlines
    line = line.rstrip()
    line = line.upper()
    print(line)
    