#Module 7 Lab
#Matt Fitzsimmons
#CIS129
#This program is designed to find the income generated from a night of sales at a dramatic theater.
#Designed to use multiple functions, to validate, to compare, to update and display strings with dynamiac variables. I think that sounds right. Haha.

#Establishing a list to allow for ease of access and customizability.
SECTION_ = ['A', 'B', 'C']
SEATS_ = [300,500,200]
PRICES_ = [20,15,10]

#This function will search through the users input character by character to ensure it matches its list.
def validNumber(userInput):
    #f will search through the list. 
    f = 0
    
    #While will make sure f stops when the text is done.
    while f < len(userInput):     
        if userInput[f] < '0' or userInput[f] > '9':
            return False
        #This will push f down the line by 1 character at the end of each loop.
        f += 1
    return True

#userParameters will allow the user to update the seat prices and maximum of seats for each section.
def userParameters(SECTION_, SEATS_, PRICES_):
    
    #Loops until userInput is recieved.
    while True:
        userInput = input('Please enter A, B, C, to edit the sections respective parameters. Type anything else to exit.')
        found = False
        
        #f will find the index of SECTION_
        f = 0
        while f < len(SECTION_):
            if SECTION_[f] == userInput:
                found = True
                break
            f += 1
            
         #This if statement will ask for the users for updatated parameters.
        if found:
            seatAmount = input(f'How many seats are in section {userInput}? ')
            seatPrice = input(f'How much does a ticket cost in section {userInput}? ')

            #Here it will check the validity of both inputs.
            if validNumber(seatAmount) and validNumber(seatPrice):
                SEATS_[f] = int(seatAmount)
                PRICES_[f] = int(seatPrice)
                print(f'Section {userInput} updating...\n')
                
            else:
                print('Error: Invalid Data Type!\nNumbers only...')
                
        else:
            break
        
    #Updates the lists with the new parameters.
    return SEATS_, PRICES_ 

#seatTicketLogic will determine if the userInput makes sense with the physical constraints of the theater.
def seatTicketLogic(abc, sectionlimit):
    while True:
        userInput = input(f'How many tickets were sold for Section {abc} (Maximum {sectionlimit}): ')
        
        #If statement to check userInput and uses the custom validNumber function to determine if it is valid.
        if validNumber(userInput):
            userInput = int(userInput)
            
            #The user cannot enter numbers bigger than seating offered by the theater or a number less than 0.
            if 0 <= userInput <= sectionlimit:
                return userInput
            
            else:
                print(f"Invalid input. Please enter a number between 0 and {sectionlimit}.")
        else:
            print('Error: Invalid Data Type! Please enter a valid positive number.')

#modeSwitch will validate userInput is either 1 or 2 when switching modes.
def modeSwitch():
    while True:
        userInput = input('Enter either 1 for edit mode or 2 for sales mode.')
        
        #Checks the userInput and compares it to 1, or 2.
        if userInput in ['1','2']:
            return int(userInput)
        
        else:
            userInput = input('Error: Invalid Data Type! Enter 1 for edit mode or 2 for sales mode: ')

def main():
    #Progam introduction
    print('Welcome to the Theater Ticket Sales program!')
    
    #Gets all global variables, updated
    global SECTION_, SEATS_, PRICES_

    while True:
        userInput = modeSwitch()
        
        #If the user inputs 1 they will be prompted to change the value of variables inside the list. 
        #The function will then update both SEATS_ and PRICES_.
        if userInput == 1:
           SEATS_, PRICES_ = userParameters(SECTION_, SEATS_, PRICES_)
            
            
        elif userInput == 2:
            print('Entering sales mode...')
            totalSales = 0
        
            f = 0
            #Most of the calculations happen here, f will keep iterating and performing the calculations for as many variables as the list holds.
            while f < len(SECTION_):
                ticketSold = seatTicketLogic(SECTION_[f], SEATS_[f])
                seatsLeft = SEATS_[f] - ticketSold
                sales = ticketSold * PRICES_[f]
                totalSales += sales
                #Receipt to display each section, sales, and seats left all dynamically.
                print(f'*---------------*\nSection {SECTION_[f]} Sales: ${sales}\n{seatsLeft} seats left.\n')
                f += 1
                
            print(f'Total Sales: ${totalSales}')
      
main()
