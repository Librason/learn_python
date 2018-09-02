from sys import argv
from os.path import exists
# exists function can tell if a file exist or not.
script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}.")
print(f"Does the input file exist? {exists(from_file)}.")
# use print(f"{exist()}.") to see if the input file exists.
in_file = open(from_file)
# in_file opened the original file.
indata = in_file.read()
# indata reads the content of the original file.
# the same content won't be copied again in a new file.
print(f"The input file is {len(indata)} bytes long.")

print(f"Does the output file exist? {exists(to_file)}.")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()

out_file = open(to_file, 'w')
# out_file opens the copied file.
out_file.write(indata)
# out_file writes the content in the original file to copied file.
print("Alright, all done.")

out_file.close()
in_file.close()
