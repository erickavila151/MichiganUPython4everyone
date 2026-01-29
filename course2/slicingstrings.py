#we can also look at any continuous section of a string using a color operator.
#the second number is one beyond the end of the slice - "up to but not including"
#if the second number is beyond the end of the string, it stops at the end.

s = "Monty Python"
print(s[0:4])
print(s[6:7])
print(s[6:20])

#if we leave off the first number or the last number of the slice, it is assumed to be the beginning or end of the string respectively