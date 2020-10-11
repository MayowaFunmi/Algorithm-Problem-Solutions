a=[]
n= int(input("Enter the number of elements in list:"))
for x in range(0,n):
    element=int(input("Enter element" + str(x+1) + ":"))
    a.append(element)
temp=a[0]
a[0]=a[n-1]
a[n-1]=temp
print("New list is:")
print(a)

'''
Program Explanation
1. User must enter the number of elements in the list and store it in a variable.
2. User must enter the values of elements into the list.
3. The append function obtains each element from the user and adds the same to the end of the list as many times as the number of elements taken.
4. A temporary variable is used to swap the first and last element in the list.
5. The newly formed list is printed.
'''