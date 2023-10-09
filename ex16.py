from sys import argv
#letting the doc know its an argument
script, filename = argv
#making a script
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
#directions for the file
input("?")

print("Opening the file...")
target = open(filename, 'w')
#opens file with words from line 5
print("Truncating the file.  Goodbye!")
target.truncate()
#deleting the file(I think)
print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()