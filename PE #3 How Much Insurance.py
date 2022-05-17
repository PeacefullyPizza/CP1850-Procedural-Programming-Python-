# Programming Exercise 3. How Much Insurance?

# Ask user for replacement cost of bulding
def askForReplacementCost():
    replacementCost = float(input("Please input the replacement cost of your building:"))
    return replacementCost

#Calculate Minimum Insurance at recommended 80%
def calculateMinimumInsurance( replacementCost ):
    minimumInsurance = replacementCost * 0.8
    return minimumInsurance

# Display the Replacement Cost and Minimum Insurance 
def printDetails ( replacementCost, minimumInsurance ):
    print("Finational experts advise that you should insure your house for:$",format(minimumInsurance,",.2f"),"\nBecause that's 80% of the replacement cost" + \
          "of your building, which is: $", format( replacementCost, ",.2f"))

def main ():
    replacementCost = askForReplacementCost()
    minimumInsurance = calculateMinimumInsurance( replacementCost )
    printDetails ( replacementCost, minimumInsurance )
main ()
