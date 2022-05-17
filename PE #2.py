# Chapter 8
# Programming Excercises 8.2
# Sum of Digits in a String

print( "This program will get the sum of digits entered.")
numberString = input( " Please enter a multi-digit number: ")

total = 0
for num in numberString:
    total += int(num)
print( "The sum of", numberString, "is", str(total) + ".")
