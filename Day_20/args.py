# *args is a parameter that allows functions to accept any number of positional arguments
# arguments passed into an atg are stored in a tuple   
# args is common name for this parameter. the * is what makes it an arg

def print_numbers(*numbers): # accept the arguments into a tuple called numbers
    #print out numbers
    for number in numbers:
        print(number)

print_numbers(1,4,5,6,7)
