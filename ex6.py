#number of people make a string for the amount of people 
types_of_people = 10
x = f"There are {types_of_people} types of people."
# more strings explaining the labels we made
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."
# just made the label for x and y
print(x)
print(y)
# telling through python that i want the string x and y to be writing in  format
print(f"I said: {x}.")
print(f"I also said: '{y}'")
#responding to the string for joke_evalution
hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"
#printing the string
print(joke_evaluation.format(hilarious))
# telling python what w and e mean 
w = "This is the left side of..."
e = "a string with the right side."

print(w + e)