a=[['A',34],['B',21],['C',26]]
for i in range(0,len(a)):
    for j in range(0,len(a)-i-1):
        if(a[j][1]>a[j+1][1]):
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
            
print(a)
# a[j] is the first list
# a[j][i] is the second element in first list
# a[j+1] is the second list
# a[j+1]
'''
Program Explanation
1. User must enter a list containing several sublists.
2. Then bubble sort is implemented to sort the list according to the second element in the sublist.
3. If the second element of the first sublist is greater than the second element of the second sublist, then the entire sublist is switched.
4. This process continues till the entire list has been sorted.
5. The sorted list is then printed.
'''