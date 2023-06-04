'''i = 0
while i<10:
    print("YES" + str(i))
    i = i+1
print("DONE")    '''

#WRITE A PROGRAM TO PRINT 1 TO50 USING A WHILE LOOP.
'''i = 1
while i<=50:
    print(i)
    i = i+1   '''

#WRITE THE PROGRAM TO PRINT CONTENT OF A LIST USING WHILE LOOP.
'''fruits = ['banana','watermelon','grapes','mangoes']
i = 0
while i<len(fruits):
    print(fruits[i])
    i = i+1
print('\n')
for items in fruits:    #USING FOR LOOP.
    print(items)   '''

#RANGE FUNCTION IN PYTHON.
'''for i in range(1,8,2):
    print(i)   '''

#FOR WITH ELSE.
'''for i in range(10):
    print(i)
else:                           #WE CAN ALSO USE ELSE WITH WHILE ALSO.
    print("This is inside else of for")   '''

#CONTINUE FUNCTION.
for i in range(10):       
    if i == 5:
        continue
    print(i)

#PASS STATEMENT IN PYTHON.(BASICALLY PASS IS A NULL STATEMENT)
i = 4
def ouch(player):
    pass

if i>0:
    pass

while i>6:
    pass
    
print("I AM A GOOD BOY")