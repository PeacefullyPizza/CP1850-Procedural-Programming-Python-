# Programming Exercises 14. Kinetic Energy

# Calculate Kinetic Energy 
def kineticEnergy( userMass, userVelocity ):
    kineticEnergy = ( 1 / 2 ) * userMass * ( userVelocity ** 2)
    return kineticEnergy

# Ask user to input Mass, and Velocity
def askUserForDetails():
    userMass = float(input( "Please enter the mass: "))
    userVelocity = float(input( "Please enter the velocity: "))
    return userMass, userVelocity

# Display The Kinetic Energy
def printDetails( userMass, userVelocity, kineticEnergy ):
    print( "The kinetic energy with mass", userMass, "and velocity", userVelocity, "is", format( kineticEnergy, ".2f" ))

def main():
    kineticEnergyCalculated = 0
    userMass, userVelocity = askUserForDetails()
    kineticEnergyCalculated = kineticEnergy( userMass, userVelocity )
    print()
    printDetails( userMass, userVelocity, kineticEnergyCalculated )

main()
