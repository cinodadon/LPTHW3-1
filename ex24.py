print("Let's practice everything ")
#telling to type whats in ()
print('You\'d need to know \'bout escapes with \\ that do:')
#print in single qoutes 
print('\n newlines and \t tabs.')
#\n=newline character/ telling function to type on new line and tab/ \t= represent a tab

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love 
nor comprehend passion from intuition 
and requires an explaination
\n\t\twhere there is none.
"""
#^\t= tab
print("--------------")
print(poem)
print("--------------")
#telling to put bar above and below the poem string

five = 10 - 2 + 3 - 6
print(f"This should be five:{five}")
#print the varible 

def secret_format(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars /100
    return jelly_beans, jars, crates 
#define secret function

start_point = 10000
beans, jars, crates = secret_format(start_point)

#remember that this is another way to format a string 
print("With a starting point of: {}".format(start_point))
#its's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10
#divide starting point by 10 

print("We can also do that this way:")
formula = secret_format(start_point)
#this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))