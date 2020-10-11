print("Enter a hyphen separated sequence of words:")
lst=[n for n in input().split('-')]  
lst.sort()
print("Sorted:")
print('-'.join(lst))

'''
Program Explanation
1. User must enter a hyphen separated sequence of words as the input.
2. The sequence is split with the hyphen as the key and the words are stored in a list.
3. The words in the list are sorted alphabetically using the sort() function.
4. The words in the list are then joined using hyphen as the reference.
6. The sorted sequence of words is then printed.
'''