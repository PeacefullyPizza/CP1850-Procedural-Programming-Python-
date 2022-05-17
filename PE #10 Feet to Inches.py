# Programming Exercises 10. Feet to Inches

# Calculation for Feet to Inches
def feetToInches( userFeet ):
    inches = ( userFeet / 1 ) * 12
    return inches

# Ask the user to enter the number of feet, then Converts and Displays
def main():
    userFeet = float(input("Please enter the number of feet: "))
    print()
    inches = feetToInches( userFeet )
    print( userFeet, "Feet converted to inches is", format( inches, ".2f"), "inches", )

main()
