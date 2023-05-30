# break statement
for i in range(1,11):
    print(i)
    if(i==5):
        break #used with a conditional statement
print("Out of the loop after 5")

# continue statement

num = int(input("Enter a number : "))
z=0
for i in range (1,11):
    z = i * num
    print (z)
    if ( z == 160):
     continue # once this condition is satisfied, the round of loop is skipped.
     # (both if statement and for loop for the satisfied condition is skipped. Rest will work as normal)
     print("this is not executed")
    print("Hello")
