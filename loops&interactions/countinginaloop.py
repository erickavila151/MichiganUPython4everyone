#this scripts counts the quantity of iterations in this loop

counter = 0
print("Before", counter)
for thing in [9, 41, 12, 3, 74, 15]:
    counter = counter + 1
    print(counter, thing)
print("After", counter)