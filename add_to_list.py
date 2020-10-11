list1 = [4,5,6,9,14]
list2 = []

x=list1[2]
list2.append(x)
print(list2)
print(list1)
print()

def add():
    y = list1[4]
    list2.append(y)
    return list2
print(add())
'''
1. Get the overall list you want to take from
2. Create a new empty list you want to add to
3. Select the item of the parent list needed and store in a variable(using slug or pk of the list item)
4. Append/Add the selected item in the new list created
5. Print out the new list 
'''