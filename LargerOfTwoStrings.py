string1=input("Enter first string:")
string2=input("Enter second string:")
count1=0
count2=0
for i in string1:
      count1=count1+1
for j in string2:
      count2=count2+1
if(count1<count2):
      print("Larger string is:")
      print(string2)
elif(count1==count2):
      print("Both strings are equal.")
else:
      print("Larger string is:")
      print(string1)
      
'''
Program Explanation
1. User must enter two strings and store it in separate variables.
2. The count variables are initialized to zero.
3. The for loop is used to traverse through the characters in the strings.
4. The count variables are incremented each time a character is encountered.
6. The count variables are then compared and the larger string is printed.'''