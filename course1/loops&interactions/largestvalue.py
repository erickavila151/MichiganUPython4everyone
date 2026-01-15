#This code is keeping track of the largest number so far in the list
largest_so_far = -1
print("Before", largest_so_far)
for the_num in [9, 41, 12, 3, 74, 15, 505, 67, 39, 72]:
    if the_num > largest_so_far :
        largest_so_far = the_num

print("After", largest_so_far)
