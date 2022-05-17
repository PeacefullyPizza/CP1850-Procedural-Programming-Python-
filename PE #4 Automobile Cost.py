# Programming Exercises 4. Automobile Costs

# Ask for monthly expenses
def askForExpenses ():
    monthlyLoanPayment = float(input("How much do you pay for your loan every month?: "))
    monthlyInsurancePayment = float(input("How much do you pay for your insurance every month?: "))
    monthlyGasPayment = float(input("How much do you pay for your gas every month?: "))
    monthlyOilPayment = float(input("How much do you pay for your oil every month?: "))
    monthlyTirePayment = float(input("How much do you pay for your tires every month?: "))
    monthlyMaintenancePayment = float(input("How much do you pay for maintenance every month?: "))
    return monthlyLoanPayment, monthlyInsurancePayment, monthlyGasPayment, monthlyOilPayment, monthlyTirePayment, monthlyMaintenancePayment

# Calculate Total Monthly Cost
def calculateTotalMonthlyCost (payment1, payment2, payment3, payment4, payment5, payment6):
    totalMonthlyCost = payment1 + payment2 + payment3 + payment4 + payment5 + payment6
    return totalMonthlyCost

# Calculate Total Annual Cost
def calculateTotalAnnualCost ( totalMonthlyCost ):
    totalAnnualCost = totalMonthlyCost * 12
    return totalAnnualCost

# Display Results
def printDetails ( totalMonthlyCost, totalAnnualCost ):
    print("\nYour total Monthly cost would be : $" + format(totalMonthlyCost,",.2f"),"\nYour total Annual cost would be : $" + format(totalAnnualCost, ",.2f"))
    
def main():
    loanPayment, insurancePayment, gasPayment, oilPayment, tirePayment, maintenancePayment = askForExpenses()
    totalMonthlyCost = calculateTotalMonthlyCost( loanPayment, insurancePayment, gasPayment, oilPayment, tirePayment, maintenancePayment)
    totalAnnualCost = calculateTotalAnnualCost( totalMonthlyCost )
    printDetails( totalMonthlyCost, totalAnnualCost )

main()
