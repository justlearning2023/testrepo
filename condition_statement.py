num =int(input("Enter the number:"))

if (num % 2 == 0):
    print("Number is even")
else:
    print("Number is odd")
print("End of condition") # this line of code is not part of the condition statement as indentation is different

#multiple conditional statement: check the number is positive negative or 0

if (num < 0):
    print("The number is negative")
    print("Hello")
elif(num > 0):
    print("The number is positive")
else:
    print("The number is zero")


