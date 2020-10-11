num =int(input('Enter the number of candidates: '))

all =[]    # list of all candidate's name & score
names = []    # names of candidates
scores = []    # scores of candidates
my_dict = {}
for i in range(num):
    print("For candidate ", i + 1)
    each = []
    name = input('Enter the name of candidate: ')
    score = float(input('Enter the score of student: '))
    my_dict[name] = score
    # add name and score to their respective lists
    names.append(name)
    scores.append(score)
    scores.sort()
    
    each.append(name)
    each.append(score)
    all.append(each)
# print("The list of all registered candidates and their respective marks: ", all)
# print()
# print("The names of all registered candidates: ", names)
# print()
# print("The scores of all candidates in ascending order: ", scores)
# print()
# print("Names and marks of candidates in dictionary form: ", my_dict)
# print()

all.sort(key = lambda x : x[1])
# print(all)
# print(all[-2][0])

unique = []
for x in all:
    for y in unique:
        if x not in unique:
            unique.append(x)
        elif x[1] in unique:
            print["name of the score that has duplicate: ", x[0]]
            print["score that has duplicate: ", x[1]]
            print("Name and score that is unique in duplicate: ", y)

'''
students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
students.sort(key = lambda x : x[1])

# students = [['Tina', 37.2], ['Harry', 37.21], ['Berry', 37.21], ['Harsh', 39], ['Akriti', 41]]
print(students[1])
'''