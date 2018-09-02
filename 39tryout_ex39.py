states = {
    "Oregon": "OR",
    "Florida": "FL",
    "California": "CA",
    "New York": "NY",
    "Michigan": "MI"
}
cities = {
    "CA": "San Francisco",
    "MI": "Detroit",
    "FL": "Jacksonville"
}

for x, y in list(states.items()):
    print(f"{x} is abbreviated {y}.")

# sth.items() is ued to read the items in a dict
# for x, y in list() is used 
# to get the first (key) and second items (value) in a dict

print("-" * 10)
for h, z in list(cities.items()):
    print(f"{h} has city: {z}.")

print(states.get("Oregon")) # return OR
# sth.get.(sth) is used to get the first element of a dict
print(states.get("OR")) # return None
# the second item won't be gotten

city = cities.get("CA")
if not city:
    print("No this city")
else: 
    print("We have this city")
city2 = cities.get("TX")
if not city2:
    print("No this city")
else:
    print("We have this city")

# if not (sth) is used to test if a item exits in a dict
