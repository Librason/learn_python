from sys import argv

script, filename = argv

txt = open(filename)
# open() is used to open a file but the content isn't read.
# () must be included in open().
print(f"Here's you file {filename}:")
print(txt.read())
# read() is used to read a text file. 
# () must be included in read().


print(">>>>>>> version II <<<<<<")
prompt = "Input the name of the file you want to open: \n>>> "
a = input(prompt)
text = open(a)
print(f"Here's your file {a}: ")
print(text.read())
# the opened file cannot be empty. 
# the .txt must be included. 
