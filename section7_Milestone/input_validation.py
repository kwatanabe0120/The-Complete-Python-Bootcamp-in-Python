# while loop to validate user input

def user_choise():
    choise = 'Wrong'
    accepted_values = range(0,11)
    within_range = False

    while choise.isdigit() == False or within_range == False:
        choise = input("Enter a positive number: ")
        
        # Check if input is a digit
        if choise.isdigit() == False:
            print("Invalid input. Please enter a positive number.") 
        
        # Check if input is within the accepted range
        if choise.isdigit() == True:
            if int(choise) in accepted_values:
                within_range = True
            else: 
                print("Number out of range. Please enter a number between 0 and 10.")
                within_range = False
    return int(choise)

result = user_choise()
print("You entered:", result)