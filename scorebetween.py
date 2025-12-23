
#multiway if, is only going to do 1:

score = input("Enter Score: ")
try:
    s = float(score)
except:
    print("Thats not a number, please introduce a value between 0.0 and 1.0")
    quit()
if s >=1.1:
    print("Out or range")
    quit()
if s >= 0.9:
    print("A")  
elif s >= 0.8:
    print("B")
elif s >= 0.7:
    print("C")
elif s >= 0.6:
    print("D")
elif s < 0.6:
    print("F")

