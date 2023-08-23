# String formatting in python can be done with three methods
# 1. f-strings
#2. format specifier
# 3. .format() method

# 1. f-strings
name = "jon"
message = f"Hello I'm {name}"
print(message)  #Hello I'm jon

# 3. .format() method
name="jane"
language = "python"
message = "hello i'm {}. I'm learning {}".format(name, language)
print(message) #hello i'm jane.I'm learning python


#2. format specifier
name="jane"
language = "python"
message="Hello I'm %s. I'm Learning %s" %(name, language)  #for integer we use %d
print(message)  #Hello I'm jane. I'm Learning python


