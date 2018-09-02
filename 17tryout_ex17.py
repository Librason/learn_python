from os.path import exists

print("Please input a file that you want to copy: ")
assign_file1 = input(">>> ")
#assigned file does not open at first. 
print(f"Does the input file exist?\n {exists(assign_file1)}.")

print("Please input a file that you want to copy to: ")
assign_file2 = input(">>> ")
# assigned file does not open at first.
print(f"Does the copied file exist?\n {exists(assign_file2)}.")

file_content = open(assign_file1)
# original file opens here.
file_data = file_content.read()
# the data is read here.
print(f"""Copying from the original 
file {assign_file1} to the copied file {assign_file2}.""")

copied_file = open(assign_file2, 'w')
# copied file is opened and prepared to be written here.
copied_file.write(file_data)
# copied file is written here.

print("\nAlright, it's done!")
file_content.close
copied_file.close
# Files that are opened before needed to be closed. 