print("""You enter a dark room with two doors.
      Do you go through door #1 or door #2?""")
#multiline code 
door = input("> ")

if door == "1":
    print("There's a giant  bear here eating cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")
    
    bear = input("> ")
    
    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. God job!")
    else:
        print(f"Well, doing {bear} is probaly better.")
        print("Bear runs away.")
        # yes f is used for {}
elif door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")
    
    insanity = input("> ")
    
    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
        #or is new 
    else: 
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

else:
    print("You stumble around and fall on a knife ad die. Good job!")
    #cant do 2 else in the same backet(from what ik rn) 