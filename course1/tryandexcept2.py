#3.1 Write a program to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number. Do not worry about error checking the user input - assume the user types numbers properly.

#Quick note: usually floating numbers are used for speed, temperature and so on. Never used to count money.

hrs = input("Enter Hours: ")
rate = input("Enter Rate: ")
try:
    fh = float(hrs)
    fr = float(rate)
except:
    print("Error, please enter numeric input")
    quit()
if fh > 40 :
    grosspay = fr * fh
    overtimepay = (fh - 40) * (fr * 0.5)

    totalpay = grosspay + overtimepay

else:
    totalpay = fh * fr
    
print(totalpay)





