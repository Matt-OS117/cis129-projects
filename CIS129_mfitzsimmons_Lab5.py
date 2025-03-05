#Matt Fitzsimmons
#3/3/2025
#CIS129 Lab 5

#This program will calculate the total number of bottles
#returned for the week and the amount paid out. 

totalBottles = 0
counter = 1
todayBottles = 0
totalPayout = 0
keepGoing = 'y'

#Establishing a loop for the program so we can repeat the calculations.
while keepGoing == "y":
    counter = 1
    totalBottles = 0
    #Establishing another loop to define the 7 day week for the program
    while counter <= 7:
        todayBottles = int(input(f"Please enter the no. of bottles returned for the day #{counter}:"))
        totalBottles = totalBottles + todayBottles #accumalator
        counter +=1 #increment statement to simulate the 'passage' of a day
    totalPayout = totalBottles * .1
    print(f"\nTotal number of bottles collected is {totalBottles}")
    print(f"Total paid out is ${totalPayout:,.2f}\n") 
    keepGoing = input("Do you want to enter another week's worth of data?\n(Enter y or n)\n")    