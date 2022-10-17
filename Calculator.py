logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print("Welcome to your Calculator program")
print("I'm going to need two numbers to run a set of calculations: add, subtract, multiply, or divide.")

# The add function adds two numbers
def add(x, y):
    return x + y
    # local scope; only the add() function sees x and y


# write the other three functions for subtract, multiply and divide

# Step 1: Write a subtract function that subtracts two numbers
def sub(x, y):
    return x - y



# Step 2: Write a multiply function that multiplies two numbers
def multiply(x, y):
    return x*y

# Step 3: Write a divide function that divides two numbers
def division(x, y):
    return x/y

# Start calculating
# Step 4: define a list called choice with + - * / in it
numerical_operations = ["+","-","*","/"]
keep_going = ["y", "n"]  # only tests for "n"

while keep_going != "n":

    num1 = float(input("Enter first number: "))
    choice = input("What kind of calculation? Choose one of: +, -, *, /  ")
    num2 = float(input("Enter second number: "))

    if choice == "+":
        # choice is a list with the string value for "+"
        # The test for choice returns the value True or False. If true:

        print(num1, choice, num2, "=", add(num1, num2))
        # calls the add function and passing it two parameters

    # finish the rest of the if statement for the other 3 calculations
    elif choice == "-":
        print(num1, choice, num2, "=", sub(num1, num2))
    # Step 5: write an elif for subtract
    elif choice == "*":
        print(num1, choice, num2, "=", multiply(num1, num2))
    # Step 6: write an elif for multiply
    elif choice == "/":
        print(num1, choice, num2, "=", division(num1, num2))
    # Step 7: write an elif for divide

    else:
        print("Invalid input")

    # Step 8: Close the calculator if input equals "n".
    keep_going = input("Calculate? y or n? ")
    if keep_going == "n":
        print("Closing the calculator.")

