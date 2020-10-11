a=[]
n= int(input("Enter the number of elements in list:"))
for x in range(0,n):
    element=input("Enter element" + str(x+1) + ":")
    a.append(element)
max1=len(a[0])
temp=a[0]
for i in a:
    if(len(i)>max1):
       max1=len(i)
       temp=i
print("The word with the longest length is:")
print(temp)

'''
Program Explanation
1. User must enter the number of elements in the list and store it in a variable.
2. User must enter the values of elements into the list.
3. The append function obtains each element from the user and adds the same to the end of the list as many times as the number of elements taken.
4. Assuming that the first element in the list has the longest length, its length is stored in a variable to be compared with other lengths later in the program.
5. Based on the above assumption, the first element is also copied to a temporary variable.
6. The for loop is used to traverse through the elements in the list.
7. The if statement then compares the lengths of other elements with the length of the first element in the list.
8. If the length of a particular word is the largest, that word is copied to the temporary variable.
9. The word with the longest length is printed.
'''