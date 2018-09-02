ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
print(stuff)

more_stuff = ["Day", "Night", "Song", "Frisbee",
"Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10: # while looping until 10.
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)
print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop()) # .pop() shows the last item in the list.
print(" ".join(stuff))
print("#".join(stuff[3:5]))
print("#".join(stuff[0:8])) # join items from 0 to 8


print("\n\n\n>>>>>>>>Tryout<<<<<<<<\n\n\n")
list = ["1", "2", "3", "4", "5"]
list2 = ["6", "7", "8", "9", "10"]

while len(list) < 8: # the list will still get to 8. 
    add = list2.pop()
    list.append(add)
    print(add, "\n")
    print(list, "\n")
    print(list2, "\n")
    print("-------------------\n")

# sth.append(sth) will add the item to a list 
# sth.append(sth) will delete the appended item from the original list. 
