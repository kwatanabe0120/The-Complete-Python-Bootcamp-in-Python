# while loop to validate user input

def user_choice():
    choice = 'Wrong'
    accepted_values = range(0,11)
    within_range = False

    while choice.isdigit() == False or within_range == False:
        choice = input("Enter a positive number: ")
        
        # Check if input is a digit
        if choice.isdigit() == False:
            print("Invalid input. Please enter a positive number.") 
        
        # Check if input is within the accepted range
        if choice.isdigit() == True:
            if int(choice) in accepted_values:
                within_range = True
            else: 
                print("Number out of range. Please enter a number between 0 and 10.")
                within_range = False
    return int(choice)

result = user_choice()
print("You entered:", result)