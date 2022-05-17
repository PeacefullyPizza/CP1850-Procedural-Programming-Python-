# Programming Exercises 11. Math Quiz
#Get 2 random numbers
import random

randomNumber1 = random.randint( 1, 250 )
randomNumber2 = random.randint( 1, 250 )

#Ask user what is the answer of Random number 1 + Random number 2
def askQuestion():
    global randomNumber1
    global randomNumber2
    userAnswer = int( input( "What is " + str( randomNumber1 ) + " + " + str( randomNumber2 ) + "?:" ))
    return userAnswer

# Check to see if user is right or wrong and display 
def checkAnswer( userAnswer ):
    global randomNumber1
    global randomNumber2
    correctAnswer = randomNumber1 + randomNumber2
    print()
    if userAnswer == correctAnswer:
        print("Congratulations!")
    else:
        print("That's Wrong. The correct answer is", correctAnswer )
    
def main():
    userAnswer = askQuestion()
    checkAnswer( userAnswer )

main()
