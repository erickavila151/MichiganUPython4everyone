#List - A linear collection of values by lookup by position - from zero to pretty much the infinite
#Dictionary - A linear collection of key-value pairs lookup by "tag" or "key"
#Dictionaries are the most powerful data collection.

#LISTS QUICK REVIEW

cards = list()
cards.append(25)
cards.append(78)
cards.append("random text")
cards.append(200)
#printing the complete list
print(cards)
#printing item in the position number 2 of the list 
print(cards[2])
#selecting an item in the list, and modifying it to print a different result
cards[1] = cards [1] + 2
print(cards)
#selecting another item in the list, storing it in a different variable and adding more text
text = cards[2] + " I am adding more random text"
print(text)

