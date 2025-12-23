def computepay(h, r):
    if h > 40:
        grosspay = h * r
        overtimepay = (h - 40)*(r * 0.5)
        totalpay = grosspay + overtimepay
    else:
        totalpay = h * r
    return totalpay
hrs = input("Introduce hours: ")
rate = input("Introduce rate: ")
try:
    h = float(hrs)
    r = float(rate)
except:
    print("please introduce a number")
    quit()
print("Pay", computepay(h, r))





