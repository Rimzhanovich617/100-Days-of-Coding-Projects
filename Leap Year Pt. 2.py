def is_leap(year):  #creates a function for the mathematical determination of a leap year
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month): #pass through year and months input
    if month > 12 or month < 1: #exclude these parameters for the formula
        return "Invalid Month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]   #days of the month for non-leap years
    if is_leap((year)) and month == 2:
        print("That month is a leap year")
        return "29 Days in February"
    print("That month is not a leap  year")
    return month_days[month-1]


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: ")) #user input for year
month = int(input("Enter a month: "))   #user input for month
days = days_in_month(year, month)








