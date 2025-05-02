#test and stuff 9.1
#Matt Fitzsimmons
#CIS 129

#Opens/Creates the txt file and lodes it as a file object thingy.
with open('grades.txt', 'w') as grades:
    #Endless loop to allow for any number of grades. 
    while True:
        gradeInput = input("Enter the students grade:\n(Type 'done' to finish)")
        if  gradeInput.lower() == 'done':
            break
        #For every new value we write it to the file and establish a new line afterwards.
        try:
            grade = float(gradeInput)
            grades.write(f'{grade}\n')
        #Magical function that makes life easy
        except ValueError:
            print('Invalid input!! Numbers only please!')