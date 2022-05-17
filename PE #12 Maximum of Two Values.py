# Programming Exercises 12. Maximum of Two Values

def max( firstNumber, secondNumber ):
    if firstNumber > secondNumber:
        return firstNumber
    else:
        return secondNumber

def getNumbersFromUser():
    userFirstNumber = int(input( "Please enter the first number:" ))
    userSecondNumber = int(input( "Please enter the second number:" ))
    return userFirstNumber, userSecondNumber

def main():
    userFirstNumber, userSecondNumber = getNumbersFromUser()
    print()
    print( "The greater value of", userFirstNumber, "and", userSecondNumber, "is:", max( userFirstNumber, userSecondNumber ))
    
main()
