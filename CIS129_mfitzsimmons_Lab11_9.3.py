#i think i figured it out finally 9.3
#Matt Fitzsimmons
#CIS129
#This program will take user input and store it into a CSV file
#It will be stored with the following format:
#firstname,lastname,exam1grade,exam2grade,exam3grade

#We need the csv module to be able to access and store these file types.
import csv

#Opens the CSV file in write mode within python
with open("grades.csv", mode="w", newline="") as grades:
    writer = csv.writer(grades)

    #Looping for user input. 
    while True:
        firstName = input("Enter student's first name (or 'byebye' to finish): ")
        if firstName.lower() == 'byebye':
            break
        lastName = input("Student's last name: ")
        
        #Try will convert all accepted input into integers.
        try:
            exam1 = int(input("Student Exam 1 grade: "))
            exam2 = int(input("Student Exam 2 grade: "))
            exam3 = int(input("Student Exam 3 grade: "))
        except ValueError:
            print("Invalid input!! Please enter integers!")
            continue

        #Finally writing to the CSV the input provided by the user, in the desired order.
        writer.writerow([firstName, lastName, exam1, exam2, exam3])
