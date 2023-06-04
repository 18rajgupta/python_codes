a = {1, 3, 5, 7, 1}
print(type(a))
print(a)

# THIS SYNTAX WILL CREATE AN EMPTY DICTIONARY NOT AN EMPTY SET
a = {}
print(type(a))

# AN EMPTY SET WILL BE CREATED USING THE BELOW SYNTAX
b = set()
print(type(b))

b.add(4)    # ADDING ELEMENTS IN EMPTY SET
b.add(5)
b.add(5)    # ADDING A VALUE REPEATEDLY DOES NOT CHANGES A SET
print(b)

b.add((4, 5, 6))   # WE CAN ADD TUPLE IN SET
print(b)

'''b.add({4:5})   # CANNOT ADD LIST OR DICTIONARY TO SET
print(b)   '''

print(len(b))   # PRINTS THE LENGTH OF THE SET

b.remove(5)     # REMOVES 5 FROM SET b
print(b)

b.pop()    # REMOVES ANY ARBITARY ELEMENT FROM THE SET
print(b)

b.clear()   # CLEAR THE WHOLE SET AND RETURN EMPTY SET
print(b)
