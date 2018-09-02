i = 0 
numbers = []

while i < 6:
    print(f"At the top i is {i}.")
    numbers.append(i)
    i += 1
    print("The list of all numbers we have now: ", numbers)
    print(f"At the bottom i is {i}.")

print("The numbers: ")
for num in numbers:
    print(num)
    # print(x) prints everything in a list.


x = 0
list = []
for x in range(0,6):
    print(f"\n\n At the top x is {x}.")
    list.append(x)
    x += 1
    print("The list of all numbers we have now: ", list)