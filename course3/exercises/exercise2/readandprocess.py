# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0.0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue

    value = float(line.split(":")[1])
    total = total + value
    count = count + 1

average = total / count

print("Average spam confidence:", average)


    
    
    

