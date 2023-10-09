from sys import argv
script, filename = argv
#^make agrument for the file
txt = open(filename)
#telling to open file 
print(f"Here's your file {filename}:")
print(txt.read())
#writes out what is inside of the file
print("Tpye the filename again:")
file_again = input(">")
#ask me the file name after showing what is in there
txt_again = open(file_again)
#open what was put int txt file
print(txt_again.read())
#prints out the txt file 