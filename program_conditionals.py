#WAP TO FIND GREATEST OF FOUR NUMBERS ENTERED BY THE USER.
'''num1 = int(input("Enter no. 1st:"))
num2 = int(input("Enter no. 2nd:"))
num3 = int(input("Enter no. 3rd:"))
num4 = int(input("Enter no. 4th:"))
if num1>num4:
    value1 = num1
else:
    value1 = num4

if num2>num3:
    value2 = num2
else:
    value2 = num3

if value1>value2:
    print("The greatest value is:", value1)
else:
    print("The greatest value is:", value2)   '''

# WAP TO FIND OUT WHETHER A STUDENT IS PASS OR FAIL, IF IT REQUIRES TOTAL 40% AND AT LEAST 33% IN EACH SUBJECT
# TO PASS. ASSUME 3 SUBJECTS AND TAKE MARKS AS AN INPUT FROM THE USER.
'''m1 = int(input("Marks of Physics:"))
m2 = int(input("Marks of Chemistry:"))
m3 = int(input("Marks of Maths:"))
if m1>=33 and m2>=33 and m3>=33:
    print("PASS")
elif ((m1+m2+m3)/3)>=40:
    print("PASSED")
else:
    print("FAIL")   '''

#A SPAM CONTENT IS DEFINED AS A TEXT CANTAINING FOLLOWING KEYWORDS: "MAKE A LOT OF MONEY","BUY NOW","SUBSCRIBE THIS","CLICK THIS".
#WRITE A PROGRAM TO DETECT THESE SPAMS.
'''text = input("Enter the text:")
if "make a lot of money" in text:
    spam = True
elif "buy now" in text:
    spam = True
elif "subscribe this" in text:
    spam = True
elif "click this" in text:
    spam = True
else:
    spam = False

if spam:
    print("This text is spam")
else:
    print("This text is not a spam")   '''

#WRITE A PROGRAM TO FIND A GIVEN USERNAME CONTAINS LESS THAN 10 CHARACTERS OR NOT.
'''username = input("Enter username:")
if len(username)<10:
    print("Yes, contains less than 10 characters")
else:
    print("Do not contain less than 10 characters")   '''

#WRITE A PROGRAM WHICH FINDS OUT WHETHER A GIVEN NAME IS PRESENT IN A LIST OR NOT.
'''names = ["raj","shubham","rohit","rohan","aditi","adarsh"]
name = input("Enter the name:\n")
if name in names:
    print("Your name is present in the list")
else:
    print("Your name is not present in the list")   '''

#WRITE A PROGRAM TO CALCULATE THE GRADE OF A STUDENT FROM HIS MARKS.
marks = int(input("Enter your marks="))
if 90<=marks<=100:
    print("Grade = EX")
elif marks>=80:
    print("Grade = A")
elif marks>=70:
    print("Grade = B")
elif marks>=60:
    print("Grade = C")
elif marks>=50:
    print("Grade = D")
else:
    print("Grade = F")   

