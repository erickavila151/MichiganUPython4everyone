#a parameter is a variable wich we use in the function definition. It is a "handle" that allows the code in the function to access the arguments for a particular function invocation 

#lang is the alias of the parameter

#example1
"""def greet (lang):
    if lang == "es":
        print("Hola")
    elif lang == "fr":
        print("Bonjour")
    else:
        print("Hello")

greet("es")
greet("fr")
greet("en")"""

#Often a function will take its arguments, do some computation, and return a value to be used as the value of the functions call in the calling expression. The return keyword is used for this.
#1. Stops the function
#2. Determines the residual value


#example 2

"""def greet():
    return "Hello"

print(greet(), "Gleen")
print(greet(), "Sally")"""

#A fruitful unction is one that produces a result (or a return value)
#The return statements ends the function execution and sends back the result of the function

def greet(lang):
    if lang == "es":
        return "Hola"
    elif lang == "fr":
        return "Bonjour"
    else:
        return "Hello"

print(greet("en"), "Erick")
print(greet("es"), "Erick")
print(greet("fr"), "Erick")