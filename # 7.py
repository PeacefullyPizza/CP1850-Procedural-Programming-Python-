# Chapter 7 
# Programming Excercises 7.7
# Driver's License Exam

def storeStudentAnswersInFile( fileName, correctAnswersList ):
    studentAnswersFile = open( fileName, "w" )
    numberOfQuestions = len( correctAnswersList )

    for currentUserAnswerIndex in range( numberOfQuestions ):
        userAnswer = input( "Please enter the answer for question " +\
                            str( ( currentUserAnswerIndex + 1 ) ) + ": " )
        
        studentAnswersFile.write( userAnswer + "\n" )
        
    studentAnswersFile.close()

def readStudentAnswersFromFileToList( fileName ):
    studentAnswersList = []
    studentAnswerFile = open( fileName, "r" )
    
    for studentAnswer in studentAnswerFile:
        studentAnswersList.append( studentAnswer )
        
    return studentAnswersList

def determineNumberOfCorrectAnswers( examCorrectAnswersList,\
                                     studentAnswersList ):
    correctAnswers = 0
    numberOfQuestions = len( examCorrectAnswersList )

    for currentExamQuestionIndex in range( numberOfQuestions ):
       if studentAnswersList[ currentExamQuestionIndex ] ==\
          examCorrectAnswersList[ currentExamQuestionIndex ]:
           correctAnswers = correctAnswers + 1
           
    return correctAnswers

def determineNumberOfIncorrectAnswers( numberOfCorrectAnswers, numberOfQuestions ):
    
    numberOfIncorrectAnswers = numberOfQuestions - numberOfCorrectAnswers
    
    return numberOfIncorrectAnswers

def getIncorrectlyAnsweredQuestionNumbers( examCorrectAnswersList, studentAnswersList ):
    
    incorrectQuestionNumbersList = []
    numberOfQuestions = len( examCorrectAnswersList )
    
    for currentExamQuestionIndex in range( numberOfQuestions ):
        if studentAnswersList[ currentExamQuestionIndex ] != examCorrectAnswersList[ currentExamQuestionIndex ]:
            incorrectQuestionNumbersList.append( currentExamQuestionIndex + 1 )
            
    return incorrectQuestionNumbersList

# Create function to see if student passed
def studentPassedExam( passMark, studentAnswersList ):
    if len( studentAnswersList ) >= passMark:
        return True
    else:
        return False

def printValuesInList( anyList ):
    for currentValueIndex in range( len( anyList ) ):
        print( anyList[ currentValueIndex ] )
        

# Create print results function
def printResults( numberOfCorrectlyAnsweredQuestions, numberOfIncorrectlyAnsweredQuestions,\
                 incorrectlyAnsweredQuestionNumbersList ):
    print()
    print( "Number of Correctly answered questions: " + str( numberOfCorrectlyAnsweredQuestions ),\
           "Number of Incorrectly answered questions: " + str( numberOfIncorrectlyAnsweredQuestions ), sep = "\n" )

    printValuesInList( incorrectlyAnsweredQuestionNumbersList )
    
# Create main function
def main():
    correctAnswersList = [ "A", "C", "A", "A", "D", "B", "C", "A", "C", "B",\
                           "A", "D", "C", "A", "D", "C", "B", "B", "D", "A" ]
    
    NUMBER_OF_QUESTIONS = len( correctAnswersList )
    FILE_NAME = "studentAnswers.txt"
    PASS_MARK = 15
    
    storeStudentAnswersInFile( FILE_NAME, correctAnswersList )

    studentAnswersList = readStudentAnswersFromFileToList( FILE_NAME )

    numberOfCorrectAnswers = determineNumberOfCorrectAnswers( correctAnswersList, studentAnswersList )

    numberOfIncorrectAnswers =\
                             determineNumberOfIncorrectAnswers( numberOfCorrectAnswers, NUMBER_OF_QUESTIONS )

    incorrectQuestionNumbersList =\
                                 getIncorrectlyAnsweredQuestionNumbers( correctAnswersList, studentAnswersList )

    printResults( numberOfCorrectAnswers, numberOfIncorrectAnswers, incorrectQuestionNumbersList )

    if studentPassedExam( PASS_MARK, studentAnswersList, ):
        print( "The student passed the exam" )
    else:
        print( "The student failed the exam" )
    
# Call main function
main()
                           
    
