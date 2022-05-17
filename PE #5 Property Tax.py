# Programming Exercises 5. Property Tax

# Ask User for Property Value
def askForActualValueOfProperty():
    actualValueOfProperty = float(input( "What's the actual value of the Property?:"))
    return actualValueOfProperty

# Calculation of Assessment Value
def calculateAssessmentValue( actualValueOfProperty ):
    assessmentValueOfProperty = 0.6 * actualValueOfProperty
    return assessmentValueOfProperty

# Calculation of Property Tax
def calculatePropertyTax( assessmentValue ):
    propertyTax = (assessmentValue / 100 ) * 0.72
    return propertyTax

# Display Property Value, Assessment, and Property Tax
def printDetails (userActualPropertyValue, assessmentValueOfProperty, propertyTax ):
    print("Actual Value of Property: $" + \
          format(userActualPropertyValue, ",.2f") + "\nAssessment Value of Property: $" + \
          format(assessmentValueOfProperty, ",.2f") + "\nProperty Tax: $", format(propertyTax, ",.2f" ))

def main ():
    userActualPropertyValue = askForActualValueOfProperty()
    assessmentValueOfProperty = calculateAssessmentValue( userActualPropertyValue )
    propertyTax = calculatePropertyTax( assessmentValueOfProperty)
    printDetails( userActualPropertyValue, assessmentValueOfProperty, propertyTax )

main()
