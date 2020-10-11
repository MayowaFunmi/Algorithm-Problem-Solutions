n=int(input("Enter number:"))
count=0
while(n>0):
    count=count+1
    n=n//10
print("The number of digits in the number are:",count)

'''
Program Explanation
1. User must first enter the value of the integer and store it in a variable.
2. The while loop is used and the last digit of the number is obtained by using the modulus operator.
3. Each time a digit is obtained, the count value is incremented.
4. This loop terminates when the value of the number is 0.
5. The total count of the number of digits is printed.'''