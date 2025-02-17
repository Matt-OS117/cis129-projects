#CIS129_Lab03_CoffeeShop
#Code developed by Matt Fitzsimmons
#The aim of this program is to calculate the price based on user input.
#And to return a detailed receipt with individual values such as, tax, sales, tax, and dollar totals.

#Assigning the variables to integer/float values.
CoffeePrice = int(5)
MuffinPrice = int(4)
SalesTax = float(.06)



#Displays the beginning of the question prompt
print('***************************************', 
      "\nMatt Fitz's Coffee and Muffin Shop")

#Assigning Variables to prompts for user input to determine
#number of coffees and muffins ordered.
CoffeeCount = int(input('Number of coffees bought?'))
MuffinCount = int(input('Number of muffins bought?'))

#Displays the end of the question prompt
print('***************************************')

#Assigning a variable to the totals before calculating tax.
CoffeeTotal= (CoffeeCount * CoffeePrice) 
MuffinTotal= (MuffinCount * MuffinPrice)

Total = MuffinTotal + CoffeeTotal

#Assigning a variable to the tax, so it can be displayed individually.
Tax = (Total * SalesTax)

#Assigning a variable to the tax and total added together
TotalWithTax = (Tax + Total) 

#Beginning of the receipt
print("***************************************",
      "\nMatt Fitz's Coffee and Muffin Shop Receipt")

#The body of the receipt, detailing the prices 
#individually and amounts totaled.
print(CoffeeCount,'Coffee at $5 each:$',CoffeeTotal,'.00')
print(MuffinCount,'Muffin at $4 each:$',MuffinTotal,'.00')
print('6% tax:$',Tax)
print('---------')

#The end of the receipt, signaling the end of the programs use.
print('Total: $',TotalWithTax)
print('***************************************')

