import time

def calculations():

    num1 = float(input("First number: "))
    num2 = float(input("Second number: "))
    operation = input("Operation? (add, sub, mul, div, exp) ")

    if operation == "add":

        print(f'{num1} + {num2} = {num1 + num2} ')

    elif operation == "sub":

        print(f'{num1} - {num2} = {num1 - num2} ')

    elif operation == "mul":

        print(f'{num1} * {num2} = {num1 * num2} ')

    elif operation == "div":

        print(f'{num1} / {num2} = {num1 / num2} ')

    elif operation == "exp":

        print(f'{num1}**{num2} = {num1 ** num2} ')

    else:

        print(f"Error in operation notation! {operation} is not a valid mathematical operation for this calculator!")
        time.sleep(3)
        exit()

    time.sleep(3)
    loop = input("Do you want to do another calculation? (y/n): ")

    if loop != "y":
        exit()

while True:

    calculations()