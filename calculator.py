# Name: Jamaica C. Palillo
# Section: BSCPE 1-2

# Program #5: Calculator App

# Choose one of the four math operations (Addition, Subtraction, Multiplication and Division)



def addition():
    try: 
        # Ask user for two numbers
        addend1 = float (input("Enter an Addend: "))
        addend2 = float (input ("Enter an Addend: "))
        sum = addend1 + addend2
        # Display the result
        print ("\nResult:", sum)

    except ValueError:
        print ("Error. Invalid Input.")
    

def subtraction ():

    try: 
        # Ask user for two numbers
        minuend = float (input ("Enter a Minuend: "))
        subtrahend = float (input ("Enter a Subtrahend: "))
        difference = minuend - subtrahend
        # Display the result
        print ("\nResult:", difference)

    except ValueError:
        print ("Error. Invalid Input.")
    

def multiplication():

    try: 
        # Ask user for two numbers
        factor1 = float (input ("Enter a Factor: "))
        factor2 = float ( input ("Enter a Factor: "))
        product = factor1 * factor2
        # Display the result
        print ("\nResult:", product)
    
    except ValueError:
        print ("Error. Invalid Input.")

         
def division():

    try:
        # Ask user for two numbers
        dividend  = float (input ("Enter a Dividend: "))
        divisor = float (input ("Enter a Divisor: "))
        quotient = dividend / divisor
        # Display the result
        print ("\nResult:", quotient)

    except ValueError:
        print ("Error. Invalid Input.")
    except ZeroDivisionError:
        print ("Rrror. Division by 0 is not allowed")

def menu():
    while True:
        # Display Greetings
        print("\n\n\033[33m" + "CALC-O-FUN")
        print("\033[33m" + "Choose the Mathematical Operation: ")

        # Display Options
        print("\n")
        print("\033[37m" + "1. Addition")
        print("\033[37m" + "2. Subtraction")
        print("\033[37m" + "3. Multiplication")
        print("\033[37m" + "4. Division")
        print("\033[37m" + "5. Quit")
        print("\n")
        user_pick = input("\033[33m" + "Please Enter a Number: " + "\033[37m")

        if user_pick == "1":
            addition()
        elif user_pick == "2":
            subtraction()
        elif user_pick == "3":
            multiplication()
        elif user_pick == "4":
            division()
        elif user_pick == "5":
            final = input("\033[32m" + "Are you sure you want to exit the program? y/n " + "\033[37m")
            if final.lower() == "y":
                print("\033[34m" + "EXITING PROGRAM. THANK YOU FOR YOUR PARTICIPATION.")
                break
            else:
                continue
        
        elif int(user_pick) > 5:
            print("Please choose only from 1-5.")
        else:
            print("\033[37m" + "Invalid. Please Choose A Number from 1-5")

        while True:
            # The application will ask if the user wants to try again or not.
            user_answer = input("\033[33m" + "\nDo you want to use the program again? y/n " + "\033[37m")

            # If yes, repeat Step 1
            if user_answer.lower() == "y":
                break

            # If no, Display "Thank You!" and the program will exit
            elif user_answer.lower() == "n":
                print("Thank You For Using the Calculator")
            else:
                print("\033[31m" + "Please enter either 'y' or 'n'." + "\033[37m")
                

menu()











