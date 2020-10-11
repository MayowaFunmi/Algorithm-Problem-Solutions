def remove(string, n):  
      first = string[:n]   
      last = string[n+1:]  
      return first + last
string=input("Enter the sring:")
n=int(input("Enter the index of the character to remove:"))
print("Modified string:")
print(remove(string, n))

'''
Program Explanation
1. User must enter a string and store it in a variable.
2. User must also enter the index of the character to remove.
3. The string and the index of the character to remove are passed as arguments to the remove function.
4. In the function, the string is split into two halves before the index character and after the index character.
5. The first half and the last half is then merged together using the ‘+’ operator.
6. The modified string is printed.'''