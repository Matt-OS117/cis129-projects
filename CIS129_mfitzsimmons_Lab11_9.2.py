#Testeeee 9.2
#Matt Fitzsimmons
#CIS129
#This program just tallys the count and calculatues the mean and total of the data.
count = 0
total = 0

#Opening the txt file

with open('grades.txt', 'r') as grades:
    for line in grades:
        #We go by line by line, stripping, printing the data.    
        try:
            grade = float(line.strip())
            print(f'{grade:.2f}')
            
            #then computing the total and tallying the count.
            total += grade
            count += 1
        except ValueError:
            print(f'Must be valid entry! Numbers only!')
            
if count > 0 :
    average = total/count
    print(f'Tota;: {total:.2f}\n')
    print(f'Count: {count}\n')
    print(f'Average : {average:.2f}\n')
else: 
    print('\nNo Valid Grades found.')