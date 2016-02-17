#Ricardo Pineda
def add( first, second):
    # TODO:
    # there's an error in this code, fix it
    return first + second # you can't put 'plus' because the program doesn't understand instead you put the symbol +

def subtract( first, second):
    # TODO:
    # fill in code here that will return the difference between first and second
    return first - second # same as add you must put the symbol to subtract the number.
def multiply( first, second):
    # TODO:
    # fill in code here that will return the product of first and second
    return first * second # this tells the program that you want to multiply the first number by the second.
def divide( first, second):
    # TODO:
    return first / second # like all other blocks this tells the program that you want to divid the first number by the second one.
    if second == 0: # this if statment will tell the program that if the second number is zero then an error will occur.
        raise Exception ("I'm sorry, I can't divide by zero.") # raising this Exception will tell the program that instead of letting the program crash it will tell the user that you "can't divid a number by zero".
        
        
    # fill in code here that:
    #   1. checks the second number to see if it is zero
    #   2. if the second number is zero, an exception is raised, the exception text must say exactly the following (make sure everything including casing and spaces match)
    #       I'm sorry, I can't divide by zero
    #   3. returns the quotient of first and second
