a=[]
n= int(input("Enter the number of elements in list:"))
for x in range(0,n):
    element=int(input("Enter element" + str(x+1) + ":"))
    a.append(element)
b=[sum(a[0:x+1]) for x in range(0,len(a))]
print("The original list is: ",a)
print("The new list is: ",b)


'''
Program Explanation
1. Use must declare a list and initialize it to an empty list.
2. Then a for loop is used to accept values for the list.
3. User must enter the number of elements in the list and store it in a variable.
4. Then the user must enter the values into the list using another for loop and insert into the list.
5. List comprehension along with list slicing is used to find cumulative sum of elements in the list
6. Then the original list and the new list is printed.
'''