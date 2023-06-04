#WRITE A PROGRAM TO PRINT THE MULTIPLICATION TABLE OF A GIVEN NUMBER USING FOR LOOP.
'''a = int(input("The table of the number:"))
for i in range(1,11):
    print(str(a) + " X " + str(i) + "=" + str(a*i))

a = int(input("The table of the number:"))     #USING WHILE LOOP.
i = 1
while i<=10:
     print(str(a) + " X " + str(i) + "=" + str(a*i))
     i = i+1   '''

#WRITE A PROGRAM TO GREET ALL THE PERSONS NAMES STORED IN A LIST L1 AND WHICH STARTS WITH S.
'''l1 = ["Harry","Sohan","Sachin","Rahul"]
for name in l1:
     if name.startswith("S"):
          print("Hello " + name)    '''

#WRITE A PROGRAM TO FIND WHETHER A GIVEN NUMBER IS PRIME OR NOT.
'''num = int(input("Enter the number="))
prime = True
for i in range(2,num):
     if num%i == 0:
          prime = False
          break
if prime:
     print("IT IS A PRIME NUMBER.")
else:
     print("IT IS NOT A PRIME NUMBER.")    '''

#WRITE THE  PROGRAM TO FIND THE SUM OF FIRST N NATURAL NUMBERS USING WHILE LOOP.
'''n = int(input("Enter the number="))
i = 1
sum = 0
while i<=n:
    sum = sum + i
    i = i+1
print("The sum is: ", sum)    '''

#WRITE A PROGRAM TO CALCULATE THE FACTORIAL OF THE GIVEN NUMBER USING FOR LOOP.
'''num = int(input("Enter the number= "))
factorial = 1
for i in range(1,num + 1):
    factorial = factorial * i

print("The factorial of the given number is= ", factorial)   '''

#WRITE A PROGRAM TO PRINT THE FOLLOWING STAR PATTERN:
for i in range(4):
    print("*" * i)

#PYRAMID.
n = 3
for i in range(3):
    print(" " * (n-i-1), end="")
    print("*" * (2*i+1), end="")
    print(" " * (n-i-1))