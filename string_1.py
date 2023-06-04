a = 18
b = "raj"
print(a ,  b)
print(type(b))
c = '''Raj"s and
       Raj's'''
print(c)   


'''#Concatanation
greeting = "Good Morning, "
name = "Raj"
d = greeting + name
print(d)   '''


name = "raj gupta gupta"
print(name[0])
#name[0] = "d"   print(name[0])    //DOES NOT WORK
print(name[0:5])        #SLICING
print(name[1:6])        #SLICING 
print(name[:5])
print(name[0:])
print(name[-5:-1])
print(name[5:0])      #WE CAN NOT PRINT REVERSE OF STRING
print(name[0:9:2])    #SLICING WITH SKIP VALUE
print(name[0:9:3])    #SLICING WITH SKIP VALUE


#STRING FUNCTIONS
print(len(name))
print(name.endswith('ta'))
print(name.endswith('jhyuf'))
print(name.count('a'))
print(name.capitalize())
print(name.find('g'))
print(name.replace('gupta','sharma'))


#ESCAPE SEQUENCES
sequence = "Raj\'s is a\ngoo\\d\tboy."     #  \n, \t, \\, \'
print(sequence)
