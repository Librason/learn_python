def print_two(arg1, arg2):
    print(f"arg1 is {arg1}, arg2 is {arg2}.")
    total = float(arg1) + float(arg2)
    print("The total of two values is: ", total)
# indentation must be included after the colon.
arg1 = input("Please input a value for arg1: ")
arg2 = input("Please input a value for arg2; ")
print_two(arg1, arg2)
arg1 = input("Please input a value for arg1: ")
arg2 = input("Please input a value for arg2; ")
print_two(arg1, arg2)
arg1 = input("Please input a value for arg1: ")
arg2 = input("Please input a value for arg2; ")
print_two(arg1, arg2)
# the def function must be defined at the end
# def cannnot be defined in terminal/powershell script. 
# every time when variables are re-defined,
# Python will run the def function again. 
