'''
You are given two integers x and y . You need to find out the ordered pairs ( i , j ) , such that ( i + j ) is not equal to n and print them in lexicographic order.( 0 <= i <= x ) and ( 0 <= j <= y) This is the code if we dont use list comprehensions in Python.
'''

x = int (input("Enter first integer: "))
y = int (input("Enter second integer: "))
n = int (input("Enter the value of n: "))
ar = []
p = 0 
for i in range ( x + 1 ):
    for j in range( y + 1):
        if i+j != n:
            ar.append([])
            ar[p] = [ i , j ]
            p+=1
print (ar)

print()

#Using list comprehension
print ([ [ i, j] for i in range( x + 1) for j in range( y + 1) if ( ( i + j ) != n )])