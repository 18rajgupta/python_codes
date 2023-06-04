# FUNCTIONS
def greet(name):
    print("Good Day, "+ name)

def mysum(num1, num2):
    return num1 + num2

greet("Raj")
s = mysum(6,32)
print(s)

# RECURSION
# n! = 1 * 2 * 3 * 4.... *n
# n! = [1 * 2 * 3 * 4... *n-1] *n
# n! = n * (n-1)!

def factorial_iter(n):
    product = 1
    for i in range(n):
        product = product * (i+1)
    return product
print(factorial_iter(5))   

def factorial_recursive(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial_recursive(n-1)
print(factorial_recursive(5))