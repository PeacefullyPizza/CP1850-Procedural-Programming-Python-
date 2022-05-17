# Chapter 7 
# Programming Excercises 7.1
# Total Sales

# Module for Days of the Week 
def enterDailySales( daysOfTheWeek ):
    dailySales = []
    # Get sales total
    for currentDay in daysOfTheWeek:
        print( "Please enter sales for", currentDay + ":", end = "" )
        dailySale = float( input() )
        dailySales.append( dailySale )
    # Return Daily Sales
    return dailySales

# Calculate the Daily Sales
def calculateWeeklySale( dailySales ):
    total = 0
    # Add totals from days entered
    for currentDailySale in range( len( dailySales ) ):
        total = total + dailySales[ currentDailySale ]
    # Return Total 
    return total

# Display Weekly Report
def printWeeklyReport( daysOfTheWeek, dailySales, totalSales ):
    print( "WEEKLY SALES REPORT\n----------------" )
    for currentDay in range( len( daysOfTheWeek ) ):
        print( daysOfTheWeek[ currentDay ] + "'s sales: ", \
               dailySales[ currentDay ] )

    print( "Total weekly sales: ", totalSales )

def main():
    daysOfTheWeek = [ "Monday", "Tuesday", "Wednesday", "Thursday", \
                      "Friday", "Saturday", "Sunday" ]
    
    dailySales = enterDailySales( daysOfTheWeek)
    totalDailySales = calculateWeeklySale( dailySales )
    printWeeklyReport( daysOfTheWeek, dailySales, totalDailySales )

main()
    
