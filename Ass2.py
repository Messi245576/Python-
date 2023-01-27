# # Files
# # Read mode
# # Write mode
# # Append mode
# # Assignment 2
# Work on r+,W+,A+
# File Handling in Python | r+ and w+ Mode in File Handling
# mode
# r+ :- Read and Write mode.
# the file pointer position at the beginning of the file.
# The r+ throws an error if file does not exist.
# Opens an existing file without truncating it.
# w+ mode
# w+ :- Write & read mode.
# the file pointer position at the beginning of the file.
# The w+ creates a new file if file does not exist.
# Opens an existing fiie and truncate it first.

messi = open("messi.txt", "r+")
print(messi.read())
messi.close()

messi = open("messi.txt", "w+")
messi.write("I am Change")

messi = open("messi.txt", "r+")
print(messi.read())

messi = open("messi.txt", "a+")
messi.write("I am append")

messi = open("messi.txt", "r")
print(messi.read())
