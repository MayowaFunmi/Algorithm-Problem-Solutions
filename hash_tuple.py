x = map(float, input().split())
list1 = tuple(x)
print(hash(list1))
for i in list1:
    print(hash(i))
 print()

n = map(int, input().split())
t = tuple(n)
print(t)
print(hash(t))