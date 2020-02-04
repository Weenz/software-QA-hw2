import math

#BMI Calculator function
def bmiCalc():

    print ("")
    print ("BMI Calculator")
    print ("------------------")

    #Loop to verify integer as input for feet
    while True:
        try:
            feet = int(input("Enter your feet part of your height: "))
        except ValueError:
            print("Incorrect value, must be a number.")
            continue
        else:
            break

    #Loop to verify integer as input for inches            
    while True:
        try:
            inches = int(input("Enter the inches part of your height: "))
        except ValueError:
            print("Incorrect value, must be a number.")
            continue
        else:
            break
    
    #Loop to verify integer as input for weight
    while True:
        try:    
            weight = int(input("Enter your weight (in pounds): "))
        except ValueError:
            print("Incorrect value, must be a number.")
            continue
        else:
            break

    weight = weight * 0.45 #metric conversion 
    height = feet * 12 + inches #total height in inches
    height = height * 0.025 #metric conversion
    height = height * height #square height

    bmi = weight / height #bmi calculation
    bmi = math.ceil(bmi * 10) / 10 #keep one decimal place

    if (bmi <= 18.5):
        value = "Underweight"

    elif ( (bmi > 18.5) and (bmi < 24.9) ):
        value = "Normal Weight"
    
    elif( (bmi > 25) and (bmi < 29.9) ):
        value = "Overweight"
    
    else:
        value = "Obese"

    return (bmi, value)