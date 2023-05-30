

for i in range (10): #as no initial value, it will start from 0, and the final value is excluded.
    # So it will print from 0-9
    print(i)
print("End of first program")

#Take a number from user and run the loop until that value:
num = int(input("Enter the number:"))
for i in range(num+1):
    print (i)

# For loop with starting and final range
z = 7
for i in range(0,11):
    print(str(z) +" * " + str(i) + "= " + str(z * i))

# For loop setting the 'increment value',inside range(first value, last value,value increasing by 2)

for i in range(1,11,2):
    print(i) #print only 1 3 5 7 9

# For loop setting the 'decrement value',inside range(first value, last value,value increasing by 2)

for i in range(10,1,-2):
    print(i) #print only 10,8,6,4,2

