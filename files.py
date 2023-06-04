# USE OPEN FUNCTION TO READ THE CONTENT OF A FILE.
'''f = open ('sample.txt', 'r')  # BY DEFAULT THE MODE IS R.
# data = f.read()
data = f.read(5)   # READ FIRST FIVE CHARACTERS FROM THE FILE. 
print(data)
f.close()   '''

# READLINE() FUNCTION.
'''f = open('sample.txt', 'r')
# read first line
data = f.readline()
print(data)

# read second line
data = f.readline()
print(data)

# read third line
data = f.readline()
print(data)

# read fourth line
data = f.readline()
print(data)
f.close()   '''

# WRITTING FILES IN PYTHON.
'''f = open('another.txt', 'a')
f.write("I am appending.")
f.close()   '''

# WITH STATEMENT.     [ (DON'T NEED TO WRITE f.close() ]
with open('another.txt', 'r') as f:
    a = f.read()
print(a)
