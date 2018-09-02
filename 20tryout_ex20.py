print("\n>>>>>>>>>> Version #1 Without def <<<<<<<<<<\n")
assigned_file = input("Please enter a file that you want to print lines:\n>>> ")

file_data = open(assigned_file)
# use open() to load the data in the file. 
print("\nFirst we print the whole file: \n\n", file_data.read())
# use .read() to show the content in the file.

print("\nNow let's rewind and print three lines: \n")

file_data.seek(0)
# use .seek(0) to go to the 0 byte position of the file. 

current_line = 1
print(current_line, file_data.readline())
# use .readline() to show the content of that line. 
# .readline() must be followed the opened file. 

current_line += 1
print(current_line, file_data.readline())

current_line += 1
print(current_line, file_data.readline())


print("\n>>>>>>>>>> Version #2 With def <<<<<<<<<<\n")
assigned_file2 = input("Please input a file you want to open: \n>>>")

indata = open(assigned_file2)
 
def f(x):
    print("\nFirst look at the whole file: \n")
    print(x.read())
f(indata)
# defintion of a function must go after the function.

def h(x):
    x.seek(0)
h(indata)

def g(y, x):
    print(y, x.readline())

print("\nNow let's rewind and print three lines: \n")
# print must go after def function.
# if print is inside the def function,
# every time when the function runs, it will print again. 
y = 1
g(y, indata)

y += 1
g(y, indata)

y += 1
g(y, indata)
