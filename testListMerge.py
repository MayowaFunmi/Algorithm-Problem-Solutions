a = [3, 5, 7]
b = [2, 8, 5]

for i in range(len(a)):
    if a[i] in b:
        del a[i]
    else:
        print("no common elements")
a.extend(b)
print(a)