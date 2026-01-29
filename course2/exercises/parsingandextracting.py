
data = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
atpos = data.find("@")
print(atpos)
#position 21

sppos = data.find(" ", atpos)
print(sppos)
#21, 31

#extrae la información basandose en la posición de los carácteres
host = data[atpos+1 : sppos]
print(host)