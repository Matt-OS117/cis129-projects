#Module Lab-4
#Matthew FItzsimmons
#2/25/2025
#This program works to modify the bonus pay for a store and its employees.
#Bonus pay is determined by employee sales increase and store sales.

#Defining variables
monthlySales = 0 #monthly sales amount
storeAmount = 0 #store bonus amount
empAmount = 0 #employee bonus amount
SalesIncrease = 0 #percent of sales increase
prompt = 'How many sales were made this month?'

#Prompts the user for the monthly sales
monthlySales = float(input(prompt))

#This code determines the storeAmount bonus

if monthlySales >= 110000:
    storeAmount = 6000
elif monthlySales >= 100000:
    storeAmount = 5000
elif monthlySales >= 90000:
    storeAmount = 4000
elif monthlySales >= 80000:
    storeAmount = 3000
else: 
    storeAmount = 0

#This code gets the percent of increase in sales
salesIncrease = float(input('How much of an increase in sales was there?'))
salesIncrease = salesIncrease/100

#This code determines the empAmount bonus
if salesIncrease >= .05:
    empAmount = 75
elif salesIncrease >= .04:
    empAmount = 50
elif salesIncrease >= .03:
    empAmount = 40
else:
    empAmount = 0
    
#This code prints bonus information

print('The store bonus amount is $',storeAmount)
print('The employee bonus amount is $',empAmount)
if (storeAmount == 6000) and (empAmount == 75):
    print('Congrats! You have the highest bonus amounts possible!')
    