from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())
# f is a variable (actually a file) that represents current_file. 

def rewind(f):
    f.seek(0)
# rewind() is only a defined function, not built-in function.
# .seek(0) moves to the start of a file where is 0 byte. 

def print_a_line(line_count, f):
    print(line_count, f.readline())
# .readline shows the content of a line.  

current_file = open(input_file)

print("First let's print the whole file: \n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Lets print three lines: ")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)