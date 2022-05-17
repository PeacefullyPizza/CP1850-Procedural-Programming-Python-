# Chapter 7 
# Programming Excercises 7.6
# Larger Than n

def findAllGreaterThanNumbers( listOfNumbers, userNumber ):
    greaterThanNumbersList = []
    
    for currentNumberIndex in range( len( listOfNumbers ) ):
        if listOfNumbers[ currentNumberIndex ] > userNumber:
            greaterThanNumbersList.append( listOfNumbers[ currentNumberIndex ] )

    return greaterThanNumbersList

def getUserNumber():
    userNumber = int( input( "Please enter a number: " ) )
    return userNumber

def displayValuesInList( anyList ):
    for currentValueIndex in range( len( anyList ) ):
        if currentValueIndex == len( anyList ) - 1:
            print( anyList[ currentValueIndex ], end = "." )
        else:
            print( anyList[ currentValueIndex ], end = ", " )

def main():
    listOfNumbers = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
    
    userNumber = getUserNumber()

    greaterThanNumbersList = findAllGreaterThanNumbers( listOfNumbers, userNumber )

    if len( greaterThanNumbersList ) < 1:
        print( "There are no numbers greater than", userNumber )
    else:
        displayValuesInList( greaterThanNumbersList )
    
    
# Call main function
main()
                           
    
