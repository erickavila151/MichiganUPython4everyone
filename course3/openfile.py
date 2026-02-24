#before we can read the contents of the file, we must tell Python which file we are going to work with and what we will be doing with the file.
#This is done with the open() function
#Open returns  a "file handle" - a variable used to perform operations on the file
#if you put in a second parameter is where the 
ordertoopen = open("book1.txt")
print(ordertoopen)