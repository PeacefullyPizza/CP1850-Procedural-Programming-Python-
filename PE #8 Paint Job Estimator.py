# Programming Exercises 8. Paint Job Estimator
# Ask user for square feet of wallspace to be painted
def askForWallSpace():
    userWallSpace = float(input("Please enter the square feet of wallspace to be painted: "))
    return userWallSpace
# Ask user to enter the price of paint   
def askForPriceOfPaint():
    priceOfPaint = float(input("Please enter the price of paint: "))
    return priceOfPaint
# Calculate Paint Required 
def calculatePaintRequired( userWallSpace ):
    paintRequired = ( userWallSpace / 112 ) * 1
    return paintRequired
# Calculate Number of Labor Hours Required 
def calculateHoursOfLaborRequired( userWallSpace ):
    hoursRequired = ( userWallSpace / 112 ) * 8
    return hoursRequired
# Calculate The Cost of Paint
def calculateCostOfPaint( priceOfPaint, gallonsOfPaintRequired ):
    costOfPaint = gallonsOfPaintRequired * priceOfPaint
    return costOfPaint
# Calculate Labor Charges 
def calculateLaborCharges( hoursOfLaborRequired ):
    charge_per_hour = 35.00
    laborCharges = hoursOfLaborRequired * charge_per_hour
    return laborCharges
# Calculate The Total Cost
def calculateTotalCostOfPaintJob( laborCharges, costOfPaint ):
    totalCost = laborCharges + costOfPaint
    return totalCost
# Display The Paint Required, Hours Required, Cost of Paint, Labor Charges, and Total Cost
def printBill( paintRequired, hoursRequired, costOfPaint, laborCharges, totalCost ):
    print( "Paint required: " + format( paintRequired, ".2f"), "Hours of labor required: " + format( hoursRequired, ".2f"), \
           "Cost of the paint: $" + format( costOfPaint, ",.2f"), "Labor charges: $" + format( laborCharges, ",.2f"), \
           "Total cost of paintjob: $" + format( totalCost, ",.2f"),sep="\n")
    
def main():
    userWallSpace = askForWallSpace()
    priceOfPaint = askForPriceOfPaint()
    paintRequired = calculatePaintRequired( userWallSpace )
    hoursRequired = calculateHoursOfLaborRequired( userWallSpace )
    costOfPaint = calculateCostOfPaint( priceOfPaint, paintRequired )
    laborCharges = calculateLaborCharges( hoursRequired )
    totalCost = calculateTotalCostOfPaintJob( laborCharges, costOfPaint )
    printBill( paintRequired, hoursRequired, costOfPaint, laborCharges, totalCost )
    
main()
    
