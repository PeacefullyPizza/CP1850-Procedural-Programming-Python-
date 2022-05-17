# Programming Exercises 9. Monthly Sales Tax
# Ask user for total sales for the month
def askForTotalSales():
    totalSalesForMonth = float(input( "Please enter the total sales for the month: "))
    return totalSalesForMonth
# Calculate County Sales Tax
def calculateCountySalesTax( totalSalesForMonth ):
    countySalesTax = ( 2.5 / 100 ) * totalSalesForMonth
    return countySalesTax
# Calculate State Sales Tax
def calculateStateSalesTax( totalSalesForMonth ):
    stateSalesTax = ( 5 / 100 ) * totalSalesForMonth
    return stateSalesTax
# Calculate Total Sales Tax
def calculateTotalSalesTax( stateSalesTax, countySalesTax ):
    totalSalesTax = stateSalesTax + countySalesTax
    return totalSalesTax
# Display The County Sales Tax, The State Sales Tax, and The Total Tax
def printSalesTaxReport( countySalesTax, stateSalesTax, totalSalesTax ):
    print( "The County sales tax is: $" + format( countySalesTax, ",.2f"), "The State sales tax is: $" + format( stateSalesTax, ",.2f"), \
           "The Total sales tax is: $" + format( totalSalesTax, ",.2f"),sep="\n")

def main():
    userTotalSalesForMonth = askForTotalSales()
    countySalesTax = calculateCountySalesTax( userTotalSalesForMonth )
    stateSalesTax = calculateStateSalesTax( userTotalSalesForMonth )
    totalSalesTax = calculateTotalSalesTax( stateSalesTax, countySalesTax )
    printSalesTaxReport( countySalesTax, stateSalesTax, totalSalesTax )

main()
