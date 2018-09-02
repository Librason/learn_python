a = input("Please input the first number: ")
b = input("Please input the second number: ")
c = input("Please input the third number: ")
d = input("Please input the forth number: ")
# use input() so that the first variable does not need to be
# the name of this program.
list = (a, b, c, d)
print("list is: ", repr(list))
print(f"""The first number is {a}, the second is {b},
the third is {c}, and the forth is {d}.""")

total = float(a) + float(b) + float(c) + float(d)
print("The total is ", total)

# on the other hand, without input()
from sys import argv
x, y, z, h = argv
print("x, y, z, h represent: ", repr(argv))
# in this case, 1st variable is the name of this file.
# the order of x, y, z, h cannot be changed
# variables must be in the front.
# must have the exact number of variable input in the command line.
# by default the input is a string.
