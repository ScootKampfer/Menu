import time

num1 = float(input("First number: "))
num2 = float(input("Second number: "))
operation = input("Operation? (add, sub, mul, div, exp) ")

if operation == "add":

    print(f'{num1} + {num2} = {num1 + num2} ')
    time.sleep(3)

elif operation == "sub":

    print(f'{num1} - {num2} = {num1 - num2} ')
    time.sleep(3)

elif operation == "mul":

    print(f'{num1} * {num2} = {num1 * num2} ')
    time.sleep(3)

elif operation == "div":

    print(f'{num1} / {num2} = {num1 / num2} ')
    time.sleep(3)

elif operation == "exp":

    print(f'{num1}**{num2} = {num1 ** num2} ')
    time.sleep(3)

else:

    print(f"Error in operation notation! {operation} is not a valid mathematical operation for this calculator!")
    time.sleep(3)
