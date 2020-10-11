dic = {}
s = list()
for _ in range(int(input("Enter number of students: "))):
    name = input("Enter name of student: ")
    score = float(input("Enter score of student: "))
    
    if score in dic:
        dic[score].append(name)
    else:
        dic[score] = [name]
    print(dic)
    print()
    
    if score not in s:
        s.append(score)
        print(s)
        print()
m = min(s)
s.remove(m)
m1 = min(s)
dic[m1].sort()
for i in dic[m1]:
    print(i)