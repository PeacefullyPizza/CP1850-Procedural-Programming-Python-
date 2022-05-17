# Chapter 8
# Programming Excercises 8.8
# Word Separator

def main():
    # Open txt file to read from
    infile = open('text.txt','r')
    file = infile.readlines()
    # Set counters.
    upperCasecount=0
    lowerCasecount=0
    spaceCount=0
    digitCount=0
    for lines in file:
        for ch in lines:
            if ch.isupper():
                upperCasecount+=1
            elif ch.islower():
                lowerCasecount+=1
            elif ch.isspace():
                spaceCount+=1
            elif ch.isdigit():
                digitCount+=1
    # Display totals.
    print("Here are the totals from the Text File:", "\nUppercase Letters:",upperCasecount,"\nLowercase Letters:",\
          lowerCasecount,"\nSpace Count:", spaceCount, "\nNumber of Digits:",digitCount)

# Call main. 
main()
