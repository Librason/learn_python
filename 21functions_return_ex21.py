def add(a, b):
    print(f"Adding {a} + {b}.")
    return a + b
# return stops the def function.
def subtract(a, b):
    print(f"Substracting {a} - {b}.")
    return a - b

def multiply(a, b):
    print(f"Multiplying {a} * {b}.")
    return a * b

def divide(a, b):
    print("Dividing {} / {}.".format(a,b))



print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print("Age: {}, Height: {}, Weight: {}, IQ: {}".format(age, height, weight, iq))



print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq,2))))

print("That becomes: ", what, "Can you do it by hand?")