from sys import argv

script, user_name = argv
prompt = ">>> "
# prompt is used to pop up command line >>> for input.
# input can only be one at most.
print(f"Hi {user_name}. I'm the {script} script.")
print("I'd like to ask you a few questions.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said you {likes} about liking me.
You live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.
""")
# the input for prompt is different from each other. 