# Name: Jamaica C. Palillo
# Section: BSCPE 1-2

# Program #5: Calculator App

# Choose one of the four math operations (Addition, Subtraction, Multiplication and Division)



def addition():
    
    addend1 = float (input("1st Addend: "))
    addend2 = float (input ("2nd Addend: "))
    sum = addend1 + addend2

    print ("\nResult:", sum)

def subtraction ():

    minuend = float (input ("Minuend: "))
    subtrahend = float (input ("Subtrahend: "))

    difference = minuend - subtrahend

    print ("\nResult:", difference)

def multiplication():

    factor1 = float (input ("1st Factor: "))
    factor2 = float ( input ("2nd Factor: "))

    product = factor1 * factor2

    print ("\nResult:", product)

def division():

    dividend  = float (input ("Dividend: "))
    divisor = float (input ("Divisor: "))

    quotient = dividend / divisor

    print ("\nResult:", quotient)

def menu():
        while True:
        # Display Greetings
            print ("\n\n\033[33m" + "CALC-O-FUN")
            print ("\033[33m" + "Choose the Mathematical Operation: ")
            
            # Display Options
            print ("\n")
            print ("\033[37m" + "1. Addition") 
            print ("\033[37m" + "2. Subtraction") 
            print ("\033[37m" + "3. Multiplication")
            print ("\033[37m" + "4. Division")
            print ("\033[37m" + "5. Quit")
            print ("\n")
            user_pick = input ("\033[33m" + "Please Enter a Number: " + "\033[37m")

            if user_pick == "1":
                addition()
            elif user_pick == "2":
                subtraction()
            elif user_pick == "3":
                multiplication()
            elif user_pick == "4":
                division()
            elif user_pick == "5":
                final = input ("\033[32m" + "Are you sure you want to exit the program? y/n " + "\033[37m")
                if final.lower() == "y":
                    print ("\033[34m" + "EXITING PROGRAM. THANK YOU FOR YOUR PARTICIPATION.")
                else:
                    continue
            else:
                print ("\033[37m" + "Invalid. Please Enter a Number.")

            user_answer = input ("\033[33m" + "\nDo you want to use the program again? y/n " + "\033[37m")
            if user_answer.lower() == "y":
                continue
            else:
                ("Thank you!")
                break

menu()
# Ask user for two numbers


# Display the result

# The application will ask if the user wants to try again or not.

# If yes, repeat Step 1

# If no, Display "Thank You!" and the program will exit

