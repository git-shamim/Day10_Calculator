
from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


symbol_function_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def simple_calculator():
    print()
    print(logo)
    num = round(float(input("Let's start! Please enter a numeric value? \n : ")), 2)
    should_continue = True
    while should_continue:
        for key in symbol_function_dict:
            print(key)
        symbol = input("Pick an operation from options shown above \n : ")
        next_num = round(float(input("What is the next number? \n : ")), 2)
        function = symbol_function_dict[symbol]
        answer = round(function(num, next_num), 2)
        print("{0} {1} {2} = {3}".format(num, symbol, next_num, answer))
        next_step = input("Do you wish to use the answer value ? Enter 'Yes' to continue ").lower()
        if next_step == 'yes' or next_step == 'y':
            num = answer
        else:
            should_continue = False
            simple_calculator()


simple_calculator()
