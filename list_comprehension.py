'''You are given three integers X, Y and Z and  representing the dimensions of a cuboid along with an integer N . You have to print a list of all possible coordinates given by (i, j, k) on a 3D grid where the sum of i + j + k is not equal to N. Here 0 <= i <= X; 0 <= i <= Y; 0 <= k <= Z,
'''
x = int(input('Enter the first number: '))
y = int(input('Enter the second number: '))
z = int(input('Enter the third number: '))
n = int(input('Enter the value of n'))

print([ [i, j, k] for i in range(x + 1) for j in range(y+1) for k in range(z+1) if ((i + j + k) != n)])