i = 0 
numbers = []

while i < 6:
    #saying i less than 6 keeps the while contained !!(While function will go forver needs to be stopped)!!
    print(f"At the top i is {i}")
    numbers.append(i)
    #adding i to each number
    i = i + 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")


print("The numbers: ")

for num in numbers:
    print(num)
     