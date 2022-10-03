# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
float_weight = float(weight)
float_height = float(height)
BMI = float_weight / (float_height * float_height)
int_BMI = round(BMI)

if int_BMI <= 18.5:
    print("Your BMI is,", int_BMI, "you are underweight.")
elif 18.5 < int_BMI < 25:
    print("Your BMI is,", int_BMI, "you have a normal weight.")
elif 25 < int_BMI < 30:
    print("Your BMI is,", int_BMI, "you are slightly overweight.")
elif 30 < int_BMI < 35:
    print("Your BMI is,", int_BMI, "you are obese.")
else:
    print("Your BMI is,", int_BMI, "you are clinically obese.")