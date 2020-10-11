a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
a.sort()
print(a)
print("Largest element is:",a[n-1])

'''
Program Explanation
1. User must enter the number of elements and store it in a variable.
2. User must then enter the elements of the list one by one using a for loop and store it in a list.
3. The list should then be sorted.
4. Then the last element of the list is printed which is also the largest element of the list.
'''