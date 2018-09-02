my_name = "Librason"
my_age = 18
my_height = 173
my_weight = 60
my_eyes = "Blue"
my_teeth = "White"
my_hair = "Brown"

print(f"Let's talk about {my_name}.")
print(f"I'am {my_height} cm tall.")
print(f"I'm {my_weight} kg heavy.")
print("Actually that's not too heavy.")
print(f"I have {my_eyes} eyes and {my_hair} hair." )
print(f"My teeth are usually {my_teeth} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.")

# also can use {}.format() to format a string 
print("Let's talk about {}.".format(my_name))
print("I'am {} cm tall.".format(my_height))
print("I'm {} kg heavy.".format(my_weight))
print("Actually that's not too heavy.")
print("I have {} eyes and {} hair.".format(my_eyes, my_hair))
# format(X,Y,Z) to combine mutiple strings.
print("My teeth are usually {} depending on the coffee.".format(my_teeth))