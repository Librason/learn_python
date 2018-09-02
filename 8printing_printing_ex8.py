formatter = "{} {} {} {}"

print(formatter.format(1,2,3,4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "I am",
    "Librason,",
    "I study in",
    "Pinetree Secondary School"
))

lines = ("I am going to", "UBC",  "to study", "engineering.")
print(formatter.format(*lines)) 
# * is used in a set of data
