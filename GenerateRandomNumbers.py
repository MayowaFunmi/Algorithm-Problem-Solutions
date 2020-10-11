import random
a=[]
i = 0
count = 0

n=int(input("Enter number of elements:"))
for i in range(n):
    a.append(random.randint(1,20))
print('Randomised list is: ',a)
    

'''
Program Explanation
1. The random module is imported into the program.
2. User must enter the number of elements from the user.
3. Using a for loop, random.randint() is used to generate random numbers which are then appended to a list.
4. The arguments given inside the random.randint() function are used to specify the range to print the randomized numbers within.
5. Then the randomized list is printed.'''