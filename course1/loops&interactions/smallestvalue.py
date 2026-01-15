#this script looks in to the smallest value
"""smallest_value_so_far = 0
print("Before", smallest_value_so_far)
for number in [9, 41, 12, 3, 74, 15]:
    if number < smallest_value_so_far:
        smallest_value_so_far = number
print("After", smallest_value_so_far)"""

#A NONE VARIABLE HAS THE PROPERTY OF NO VALUE IN IT, THAT IS WHAT MAKES IT SPECIAL

#FIXED VERSION USING A NONE VARIABLE

#flag value = None
smallest_value_so_far = None
print("Before", smallest_value_so_far)
for number in [9, 41, 12, 3, 74, 15]:
    if smallest_value_so_far is None:
        smallest_value_so_far = number
    elif number < smallest_value_so_far :
        smallest_value_so_far = number
    print(smallest_value_so_far, number)
print("After", smallest_value_so_far)
