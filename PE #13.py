print("\nFor example: HELLO WORLD" )

# Have user enter sentence. 
sentence = input( "Please enter your sentence in uppercase letters: ")

 
# Split the sentence into a list of words.
words = sentence.split(' ')
 
# Empty list to contain the Pig Latin words.
newWords = []
 
# Convert each word to Pig Latin and add to new_words.
for word in words:
    if word[-1].isalpha():
        newWords.append(word[1:] + word[0] + 'AY')
    else:
        newWords.append(word[1:-1] + word[0] + 'AY' + word[-1])      
 
# Join the list back together with the space character.
newSentence = ' '.join(newWords)
 
# Display the new sentence in Pig Latin.
print("\nHere\'s your sentence written in Pig Latin: ")
print(newSentence)
