# Programming Exercises 7. Stadium Seating

# Calculate Class A Ticket Sales
def calculateClassATicketSales( classATicketsBought ):
    classASales = classATicketsBought * 20
    return classASales

# Calculate Class B Ticket Sales
def calculateClassBTicketSales( classBTicketsBought ):
    classBSales = classBTicketsBought * 15
    return classBSales

# Calculate Class C Ticket Sales
def calculateClassCTicketSales( classCTicketsBought ):
    classCSales = classCTicketsBought * 10
    return classCSales

# Calculate Total Ticket Sales
def calculateTotalSales( classASales, classBSales, classCSales ):
    totalSales = classASales + classBSales + classCSales
    return totalSales

# Display Total Class A Sales, Total Class B Sales, Total Class C Sales, and Total Ticket Sales
def printSalesReport( classASales, classBSales, classCSales, totalSales):
    print( "Class A Sales: $" + format( classASales, ",.2f"), \
           "Class B Sales: $" + format( classBSales, ",.2f"), \
           "Class C Sales: $" + format( classCSales, ",.2f"), \
           "Total sales: $" + format( totalSales, ",.2f"),sep="\n")

def main():
    classATicketsBought = int(input("How many tickets were bought for class A: "))
    classBTicketsBought = int(input("How many tickets were bought for class B: "))
    classCTicketsBought = int(input("How many tickets were bought for class C: "))
    classASales = calculateClassATicketSales( classATicketsBought )
    classBSales = calculateClassBTicketSales( classBTicketsBought )
    classCSales = calculateClassCTicketSales( classCTicketsBought )
    totalSales = calculateTotalSales( classASales, classBSales, classCSales )
    printSalesReport( classASales, classBSales, classCSales, totalSales )

main()
   
