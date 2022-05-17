# Chapter 7 
# Programming Excercises 7.2
# Lottery Number Generator 

# Get Random Number
import random 

# Random number in range 0-9
def generateRandomNumber():
    randomNumber = random.randint( 0, 9 )
    return randomNumber

def generateLotteryNumbers( numberOfLotteryNumbers ):
    # Create empty list
    lotteryNumbers = []

    for lotteryNumberIndex in range( numberOfLotteryNumbers ):
        randomNumber = generateRandomNumber()
        lotteryNumbers.append( randomNumber )
    return lotteryNumbers

def printLotteryNumbers( lotteryNumbers ):
    for currentLotteryNumberIndex in range( len(lotteryNumbers ) ):
        print( lotteryNumbers[ currentLotteryNumberIndex ], end = ", " )

def main():
    numberOfLotteryNumbers = 7
    lotteryNumbers = []
    lotteryNumbers = generateLotteryNumbers( numberOfLotteryNumbers )
    print( "\nThese are your Lottery Numbers:\n ")
    printLotteryNumbers( lotteryNumbers )

main()
