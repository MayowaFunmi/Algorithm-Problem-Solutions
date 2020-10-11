a=[]
c=[]
n1=int(input("Enter number of elements:"))
for i in range(1,n1+1):
    b=int(input("Enter element:"))
    a.append(b)
n2=int(input("Enter number of elements:"))
for i in range(1,n2+1):
    d=int(input("Enter element:"))
    c.append(d)
new=a+c
new.sort()
print("Sorted list is:",new)

'''
Program Explanation
1. User must enter the number of elements for the first list and store it in a variable.
2. User must then enter the elements of the list one by one using a for loop and store it in a list.
3. User must similarly enter the elements of the second list one by one.
4. The ‘+’ operator is then used to merge both the lists.
5. The sort function then sorts the list in ascending order.
6. The sorted list is then printed.'''