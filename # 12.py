# Chapter 7 
# Programming Excercises 7.12
# Prime Number Generation

# To take input from the user
num = int(input("Enter a number: "))
print()
# prime numbers are greater than 1
if num > 1:
   # check for factors
   for i in range(2,num):
       if (num % i) == 0:
           print(num,",is not a prime number")
           print(i,"times",num//i,"is",num)
           break
   else:
       print(num,",is a prime number")
       
# if input number is less than
# or equal to 1, it is not prime
else:
   print(num,"is not a prime number")

print("Prime numbers up to", num, ":" )
print()

for num in range(0, num + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
