people = 30
cars = 40
trucks = 15 

if cars > people:
    print("We should take the cars")
    #if cars are greater than people 
    
elif cars < people:
    print("We should  not take the cars.")
     #excute code if cars<people is true 
else:
    print("We can't decide.")
    #if cars<people isn't true print this string

if trucks > cars:
    print("Thats's to many trucks.")
elif trucks <  cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
