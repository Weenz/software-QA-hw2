import math
from bmiCalc import *
from retirementCalc import *

option = 1

while (option != 3):
    print ("--------------------------------")
    print ("|                              |")
    print ("|   Software QA Assignment 2   |")
    print ("|                              |")
    print ("--------------------------------")
    print ("--------------------------------")
    print ("| Select an option from below: |")
    print ("|                              |")
    print ("|   1.  BMI Calculator         |")
    print ("|   2.  Retirement Calculator  |")
    print ("|   3.  Exit                   |")
    print ("|                              |")
    print ("--------------------------------")

    #These two while statements verify the user input
    while True:
        try:
            option = int(input("Select an option: "))
        except:
            print ("Must be a number value!")
            continue
        else:
            break

    while ( (option < 1) or (option > 3) ):
        print ("Must be a valid option choice!")

        while True:
            try:
                option = int(input("Select an option: "))
            except:
                print ("Must be a number value!")
                continue
            else:
                break


    #Option 1: BMI Calculator
    if (option == 1):
        print ("Results: ", bmiCalc())
        
        print ("")
        input ("Press enter to return to selection screen...")
        print ("")

    #Option 2: Retirement Calculator
    elif (option == 2):
        age = retirementCalc()
        if (age >= 100):
            print ("You died at 100 before reaching your goal.")
            print ("You would have hit your goal at age", age)
        
        elif (age == 0):
            print ("Error: Annual salary or the percentage saved cannot be zero")
        
        else:
            print ("")
            print ("You will reach your goal at age", age)
        
        print ("")
        input ("Press enter to return to selection screen...")
        print ("")

print ("")
print ("Have a nice day!")
input ("Press Enter to close the application...")
