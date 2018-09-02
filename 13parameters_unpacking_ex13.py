from sys import argv
# read the WYSS for how to run this 
script, first, second, third = argv
# four variables: script, first, second and third
# the first one must be script while first, second and third
# can be anything like apple, orange etc. 
print("Tne script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)
# must have 3 variables input. 
print("argv represents:", repr(argv))
# repr means represent.
# use print(repr()) to print the variable to debug.