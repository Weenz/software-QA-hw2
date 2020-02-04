import math

def retirementCalc():

    #Loop to verify int for age
    while True:
        try:
            age = int(input("Wheat is your age? "))
        except ValueError:
            print("Incorrect value, must be a number.")
            continue
        else:
            break

    #Loop to verify int for salary
    while True:
        try:
            aSalary = int(input("What is your annual salary? "))
        except ValueError:
            print("Incorrect value, must be a number.")
            continue
        else:
            break

    #Loop to verify int for percentage saved
    while True:
        try:
            percentSaved = int(input("What is the percentage saved? "))
        except ValueError:
            print("Incorrect value, must be a number.")
            continue
        else:
            break

    #Loop to verify int for user's goal
    while True:
        try:
            userGoal = int(input("What is your savings goal? "))
        except ValueError:
            print("Incorrect value, must be a number.")
            continue
        else:
            break

    yearsReq = int(userGoal / (aSalary * ((percentSaved/100) * 1.35)))

    goalAge = int(math.ceil(age + yearsReq))

    return goalAge