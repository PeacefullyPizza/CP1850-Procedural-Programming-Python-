# Programming Exercises 2. Sales Tax Program Refactoring
def askAmountOfPurchase():
    userAmountOfPurchase = float(input("Please enter the amount of purchase:"))
    return userAmountOfPurchase

#calculate State Tax
def calculateStateTax ( userAmountOfPurchase ):
    state_tax = 0.05 * userAmountOfPurchase
    return state_tax

#calculate County Tax
def calculateCountyTax ( userAmountOfPurchase ):
    county_tax = 0.025 * userAmountOfPurchase
    return county_tax

#calculate Total Tax
def calculateTotalTax ( state_tax, county_tax ):
    total_tax = state_tax + county_tax
    return total_tax

#calculate Total Sale
def calculateTotalSale ( userAmountOfPurchase, total_tax ):
    total_sale = userAmountOfPurchase + total_tax
    return total_sale

#Display taxs, and total 
def printDetails( userAmountOfPurchase, state_tax, county_tax, total_tax, total_sale ):
    print("User amount of purchase: $" + \
          format(userAmountOfPurchase, ",.2f"),"State Tax: $" + \
          format(state_tax, ",.2f"),"County Tax: $" + \
          format(county_tax, ",.2f"),"Total Tax: $" + \
          format(total_tax,",.2f"),"Total Sale: $" + \
          format(total_sale,",.2f"), sep="\n" )
    
def main ():
    userAmountOfPurchase = askAmountOfPurchase()
    state_tax = calculateStateTax( userAmountOfPurchase )
    county_tax = calculateCountyTax( userAmountOfPurchase )
    total_tax = calculateTotalTax( state_tax, county_tax )
    total_sale = calculateTotalSale( userAmountOfPurchase, total_tax )
    printDetails( userAmountOfPurchase, state_tax, county_tax, total_tax, total_sale)
main()




