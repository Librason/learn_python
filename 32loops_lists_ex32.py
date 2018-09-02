the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']


for a in the_count:
    print(f"This is count {a}.")
# for a(or any variables) in sth(a list):
# for loop will run many times as long as the condition is met.

for fruits in fruits:
    print(f"A fruit of types: {fruits}.")

# we can also go through mixed lists
# we have to use {} since we don't know what's in it.
for i in change:
    print(f"I got {i}.")

# we can build lists, first starting with an empty one.
elements = []

# then use the range function to do 0 to 5 counts.
#The last number doesn't count. 
for i in range(0,6): #(0,6) is 0, 1, 2, 3, 4, and 5, no 6
    print(f"Adding {i} to the list.")
    # append is a function that lists understand
    elements.append(i)
    # use .append(sth) to add items to a list.
    # .append() must in the for loop because it needs to run multiple times. 
for i in elements:
    print(f"Elements was: {i}.")



cousins = []
for x in range(1,4):
    print(x)
    cousins.append(x)
print(f"I have three cousins in my family.")
for z in cousins:
    print(f"The {z} cousin.")
