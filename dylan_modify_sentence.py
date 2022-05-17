# Create main.
def main():
    # Have user enter sentence.
    userSentence = input( "Please enter a full sentence:" )
    # Make sentence all lowercase.
    lowerSentence = userSentence.lower()
    # Make sentence all uppercase.
    upperSentence = userSentence.upper()
    # Make sentence replace all "a" characters with "z" characters.
    replaceSentence = userSentence.replace("a", "z")

    #Display sentences.
    print( "\nHere is your sentence: ", "\n", userSentence)
    print( "\n", lowerSentence )
    print( "\n", upperSentence )
    print( "\n", replaceSentence )

# Call main.
main()
