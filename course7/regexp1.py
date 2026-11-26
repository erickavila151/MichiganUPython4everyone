#REGULAR EXPRESSIONS GUIDE

# ^ ->  Matches the beggining of a line
# $ ->  Matches the end of the line
# . ->  Matches any character
# \s -> Matches withespace
# \S -> Matches any non-whitespace character
# * ->  Repeats a character zero or more times
# *? -> Repeats a character zero or more times (non-greedy)
# + ->  Repeats a character one or more times
# +?->  Repeats a character one or more times (non-greedy)
# [aeiou] ->  Matches a single character in the listed set
# [^XYZ] ->  Matches a single character not in the listed set
# [a-z0-9] -> The set of character can include a range
# ( -> Indicates where string extraction is to start
# ) -> Indicates where string extraction is to end

#Before we can use regular expressions we need to import the library import re