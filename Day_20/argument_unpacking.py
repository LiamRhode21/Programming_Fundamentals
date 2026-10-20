# This function expects 2 arguments: name and age
def show_info(name, age):
    print(f"{name} is {age} years old")

# store the person info in a tuple
person = ("Alice", 30)

# * unpacks the tuple into separate positional arguments
show_info(*person) 

# person info in a dictionary
person_dictionary =  {"name":"bob", "age":25}

# this unpacks the dictionary into separate keyword arguments
show_info(**person_dictionary)

# In a function definition(as parameters), *args and **kwargs collect arguments.
# in a function call, * and ** unpack values