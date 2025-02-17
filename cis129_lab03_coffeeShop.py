#CIS129_Lab03_CoffeeShop
#Code developed by Matt Fitzsimmons
#The aim of this program is to calculate the price based on user input.
#And to return a detailed receipt with individual values such as, tax, sales, tax, and dollar totals.

#Assigning the variables to integer/float values.
CoffeePrice = int(5)
MuffinPrice = int(4)
DanishPrice = int(6)
BiscottiPrice = float(.65)
SalesTax = float(.06)



#Displays the beginning of the question prompt
print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*', 
      "\nFitz's Coffee and Muffin Shop",
      "\nIt's great when you pretend to spend!")

#Assigning Variables to prompts for user input to determine
#number of coffees and muffins ordered.
CoffeeCount = int(input('Number of coffees purchased?'))
MuffinCount = int(input('Number of muffins purchased?'))
DanishCount = int(input('Number of danishes purchased?'))
BiscottiCount = int(input('Number of biscotti purchased?'))

#Displays the end of the question prompt
print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')

#Assigning a variable to the totals before calculating tax.
CoffeeTotal = (CoffeeCount * CoffeePrice) 
MuffinTotal = (MuffinCount * MuffinPrice)
DanishTotal = (DanishCount * DanishPrice)
BiscottiTotal = (BiscottiCount * BiscottiPrice)

Total = MuffinTotal + CoffeeTotal + BiscottiTotal + DanishTotal

#Assigning a variable to the tax, so it can be displayed individually.
Tax = (Total * SalesTax)

#Rounding the Tax float number so it doesn't calculate the entire irrational number.
RoundedTax = round(Tax, ndigits=2)

#Assigning a variable to the tax and total added together
TotalWithTax = (Tax + Total) 

#Beginning of the receipt
print("\n*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*",
      "\nFitz's Coffee and Muffin Shop Receipt")

#An extra challenge I wanted to add, using an if statement to differentiate between a good deal or not.

if TotalWithTax > int(20):
      print('Yikes! The economy is tough right now!')
if TotalWithTax < int(20):
      print('Sweet! You got a good deal!')
      
#The body of the receipt, detailing the prices 
#individually and amounts totaled.
print(CoffeeCount,'Coffee at $5 each:$',CoffeeTotal,'.00')
print(MuffinCount,'Muffin at $4 each:$',MuffinTotal,'.00')
print(DanishCount,'Danish at $6 each:$',DanishTotal,'.00')
print(BiscottiCount,'Biscotti at $.65 each:$',BiscottiTotal,'.00')
print('6% tax:$',RoundedTax)
print('---------')

#The end of the receipt, signaling the end of the programs use, and thanking the user.
print('Total: $',TotalWithTax)
print("Thank you for choosing, Fitz's Coffee and Muffin Shop.")
print('Come back soon and we still might be in business!')
print('*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*')
