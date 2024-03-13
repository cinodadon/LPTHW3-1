from sys import exit

print("""You have 2 roads, a red road and a blue road. Which road do you take.""")

road = input("> ")

if road == "red":
    print("You see 6 women.")
    print("What do you do?")
    print("1. you help take the women home.")
    print("2. Continue on your way.")
    
    action = input("> ")
    
    if action == "1":
       print("How many will you take? Enter a number between 1 and 6.")
       taken_number = input("> ")
       
       if taken_number.isdigit():
           taken_amount = int(taken_number)
           
           if 1 <= taken_amount <= 6:
               print(f"You decide to take {taken_amount} women home.")
               #if you picka number bwtween 1-6 you continue
else:
        print("Please enter a number 1-6.")
        #if you pick a number outside of 1-6 this message will pop up
        
        
        
            
    
    