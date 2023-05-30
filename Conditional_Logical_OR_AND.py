# Conditional OR
# Enter marks and if marks > 100 or marks < 0 print invalid
# If not invalid display the marks
marks = int(input("Enter the marks : "))

if (marks > 100 or marks < 0):
    print("The mark entered is invalid")
else:
    print("The mark is : "+str(marks))
# Conditional AND
# Check the number whether its +ve and multiple of 2, then print as even number
# Check the number whether its +ve and not multiple of 2, then print as odd number

num = int(input("Enter the number : "))

if ((num > 0) and (num % 2 == 0)):
    print("The number is even number")
elif((num > 0) and (num % 2 == 1)):
    print("The number is odd number")


