# WRITE A PROGRAM USINF FUNCTION TO FIND GREATEST OF THREE NUMBERS.
'''def greatest(num1, num2, num3):
    if num1>num2:
        return num1
    else:
        return num2
    if num2>num3:
        return num2
    else:
        return num3

m = greatest(33,7656,5)
print("The greatest number is= " + str(m))   '''

# WRITE A PYTHON PROGRAM USING FUNCTION TO CONVERT CELCIUS TO FAHRENHEIT.
'''def fahrenheit(cel):
    return (cel * (9/5)) + 32

c = 0
f = fahrenheit(c)
print("Fahrenheit temperature is= " + str(f))    '''

# HOW DO YOU PREVENT A PYTHON PRINT() FUNCTION TO PRINT A NEW LINE AT THE END.
'''print("Hello," , end = " ")
print("How" , end = " ")
print("are" , end = " ")
print("you?" , end = " ")   '''

# WRITE A RECURSIVE FUNCTION TO CALCULATE THE SUM OF FIRST N NATURAL NUMBERS.
'''def sum(n):
    if n == 1:
        return 1
    return n + sum(n-1)
s = sum(6)
print("Sum of n natural numbers= " + str(s))   '''

# WRITE A PYTHON FUNCTION TO PRINT FIRST N LINES OF THE FOLLOWING PATTERN:
'''  * * *
     * *
     *          '''
'''def pattern(n):
    for i in range(n):
        print("*" * (n-i))

pattern(5)   '''

# WRITE A PYTHON FUNCTION TO REMOVE A GIVEN WORD FROM A STRING AND STRIP IT AT THE SAME TIME.
def remove_strip(string, word):
    newstr = string.replace(word, "")
    return newstr.strip()

string = "     Raj is a good boy          "
n = remove_strip(string, "Raj")
print(n)

#WRITE A PYTHON FUNCTION TO PRINT MULTIPLICATION TABLE OF A GIVEN NUMBER.
def table(n):
    for i in range(1,11):
        print(n * i)
    
print("The multiplication table of given number=")
print(table(5))
