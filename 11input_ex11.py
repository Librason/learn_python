print("How old are you?", end = ' ')
# end = ' ' joins print and input into one line.
age = input()
print("How tall are you?", end = ' ')
height = input()
print("How much do you weight", end = ' ')
weight = input()

print(f"So, you're {age} years old, {height} tall and {weight} heavy.")

# input() is a string by default
# if math is needed, use int(input())  
# or float(input()) to make it a number. 