print("Please input the file that you want to re-write.")
file_name = input(">>> ")
print(f"You are re-writing the file: {file_name}.")
print("If you want to do that, hit RETURN.")
print("If you don't want to do that, hit CTRL.")
input("?")
print("Opening the file...")

target = open(file_name, 'w')
print("Truncating the file...")
target.truncate()
# .truncate() is used to erase a file.
print(f"Now please enter three lines into {file_name} file. ")
prompt2 = "Please input content into a line \n>>> "
line1 = input(prompt2)
line2 = input(prompt2)
line3 = input(prompt2)

print(f"The file {file_name} is being re-writed.")
target.write(line1)
# .write() can only include one argument. 
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("Finally, the file is closed.")
target.close()
# if no existing file is selected, Python will create a new file. 
