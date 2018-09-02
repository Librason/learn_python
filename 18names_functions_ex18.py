# this is like scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}.")

# that *argv is actually pointless, we can do this
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}.")

# this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}.")

# this takes no arguments
def print_none():
    print("I got nothing.")

print_two("Librason", "Chen")
print_two_again("Librason", "Chen")
print_one("First!")
print_none()

# def function sets a defined function in Python
# every time the variables are defined, def will execute again.
