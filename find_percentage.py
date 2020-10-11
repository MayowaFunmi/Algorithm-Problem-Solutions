from decimal import Decimal

n = int(input("Enter number: "))
student_marks = {}
for _ in range(n):
    name, *line = input('Enter name: ').split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input('Enter name to query: ')
add_mark = sum(student_marks[query_name])

avg = add_mark / len(student_marks[query_name])
num = Decimal(str(avg))
print(avg)
print(round(num, 2)) # 2 d.p

#print(student_marks[query_name])
#print(student_marks)