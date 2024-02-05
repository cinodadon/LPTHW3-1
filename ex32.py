the_count = [1,2,3,4,5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']
 
 #this first kind of for-loop goes through a list
 
for number in the_count:
    print(f"This is count {number}")
    #remember that f is for {}

#same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")


#also we can go through mixeed lists too
#also notice we have to use {} since we don't know what's in it
for i in change:
    print(f"I got {i}")

#we can also build lists, first start with an empty one
elements = []

#then use the range function to do 0 to 5 count 
for i in range(0,6):
    print(f"Ading {i} to the list.")
    #append is a function that lists understand
    elements.append(i)
    #range 0,6 is only 5 bc 0 counts as 1 
    
#now we can print them out too
for i in elements:
    print(f"Elenent was: {i}")
    #i dont have to make a for-loop and can elements = list(range(0, 6))
    