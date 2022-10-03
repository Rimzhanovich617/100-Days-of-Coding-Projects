print("Welcome to the Tip Calculator.")
print("What was the total bill? ")
total_bill = input()
float_total_bill = float(total_bill)
print("How many split the bill? ")
people = int(input())
print("What percentage tip would you like to give? 10, 12, or 15?")

tip_percent = int(input())
formula1 = float_total_bill * tip_percent
formula2 = formula1/100
formula3 = float_total_bill + formula2
tip_formula = (formula3)/people
formatted_tip_formula = "{:.2f}".format(tip_formula)
print("Each person should pay: $", formatted_tip_formula)