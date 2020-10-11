'''
s = input()
def func(s):
    for i in range(len(s)):
        if s[i].isalnum():
            return True
            break
    return False
    
def func2(s):
    for i in range(len(s)):
        if s[i].isalpha():
            return True
            break
    return False
    
def func3(s):
    for i in range(len(s)):
        if s[i].isdigit():
            return True
            break
    return False
    
def func4(s):
    for i in range(len(s)):
        if s[i].islower():
            return True
            break
    return False
    
def func5(s):
    for i in range(len(s)):
        if s[i].isupper():
            return True
            break
    return False
    
print(func(s))
print(func2(s))
print(func3(s))
print(func4(s))
print(func5(s))
'''
s = "school54"
c_list = []
for char in s:
    c_list.append(char)
print("List of characters: ")
print(c_list)

for x in s:
    if x.isalnum():
        print("Any character: True")
        break
    else:
        print("Character: False")
        break
print()

for x in s:
    if x.isalpha():
        print("Any alphabeth: True")
        break
    else:
        print("Alphabeth: False")
        break

print()
for x in s:
    if x.isdigit():
        print("Any digit: True")
        break
    else:
        print("Digit: False")
        break

print()        
for x in s:
    if x.islower():
        print("Small letters: True")
        break
    else:
        print("Letters: False")
        break

print()
for x in s:
    if x.isupper():
        print("Capital letters: True")
        break
    else:
        print("Capital Letters: False")
        break

'''
S = "school"
print (any([char.isalnum() for char in S]))
print (any([char.isalpha() for char in S]))
print (any([char.isdigit() for char in S]))
print (any([char.islower() for char in S]))
print (any([char.isupper() for char in S]))
'''