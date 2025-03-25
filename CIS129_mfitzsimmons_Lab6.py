#Hotdog Cookout Lab6
#Matt Fitzsimmons
#This program attempts to calculate the necessary amount of hot dogs and buns respectively needed for a cookout

DOGS = 10 #Amount of hotdogs in a package
BUNS = 8 #Amount of buns in a package
    

def getTotalHotDogs():
    #Get the number of people attending the cookout
    People = int(input('Enter many people are attending the cookout:'))
    #Get the number of hotdogs each person will recieve
    Hot_dogs = int(input('Enter the number of hot dogs for each person:'))
    
    #Total number of hotdogs needed is calculated
    total = People * Hot_dogs
    return total 

def ShowResults(dogsLeft, minDogs, bunsLeft, minBuns):
    print(f'Minimum packages of hot dogs needed: {minDogs}')
    print(f'Minimum packages of hot dogs buns needed: {minBuns}')
    print(f'Hot dogs left over: {dogsLeft}')
    print(f'Hot dogs buns left over: {bunsLeft}')

def main():
    #Number of total got dogs needed
    total = getTotalHotDogs()

    #Calculate leftover hot dogs
    dogsLeft = (DOGS - total % DOGS) % DOGS

    #Minimum packages of Hot Dogs
    minDogs = (total + DOGS - 1) // DOGS

    #Leftover hot dog buns
    bunsLeft = (BUNS - total % BUNS) % BUNS 

    #Minimum packages of buns
    minBuns = (total + BUNS - 1) // BUNS

    #Display results
    ShowResults(dogsLeft, minDogs, bunsLeft, minBuns)

main()